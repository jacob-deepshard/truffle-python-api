import socket
import threading
import time
import socket
import threading
from typing import Optional

import truffle.protos.client_pb2  # Generated from your client.proto
import truffle.protos.app_pb2  # Generated from your app.proto

class TruffleClient:
    def __init__(self):
        self.socket = None
        self.host = ""
        self.port = 3001
        self.connected = False
        self.receive_thread = None
        self.running = False

    def connect(self, host: str):
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)  # Set a timeout for connection attempts
        try:
            self.socket.connect((self.host, self.port))
            self.connected = True
            self.running = True
            self.receive_thread = threading.Thread(target=self._receive_messages, daemon=True)
            self.receive_thread.start()
        except socket.error as e:
            self.connected = False
            raise ConnectionError(f"Failed to connect to {self.host}:{self.port} - {e}")

    def disconnect(self):
        self.running = False
        if self.socket:
            self.socket.close()
        self.connected = False

    def send_wifi_credentials(self, ssid: str, password: str, truffle_name: Optional[str] = None):
        if not self.connected:
            raise ConnectionError("Not connected to Truffle device.")

        settings = client_pb2.SetSettings()
        settings.wifi_ssid = ssid
        settings.wifi_pwd = password
        if truffle_name:
            settings.truffle_name = truffle_name
        settings.get_settings = True  # Request current settings after update

        message = client_pb2.ClientMessage()
        message.settings.CopyFrom(settings)

        self._send_message(message)

    def _send_message(self, message):
        data = message.SerializeToString()
        # Prepend the message length for framing
        msg_length = len(data).to_bytes(4, byteorder='big')
        self.socket.sendall(msg_length + data)

    def _receive_messages(self):
        while self.running:
            try:
                # Receive message length
                raw_msglen = self._recvall(4)
                if not raw_msglen:
                    break
                msglen = int.from_bytes(raw_msglen, byteorder='big')
                # Receive the actual message
                data = self._recvall(msglen)
                if data:
                    self._process_received_data(data)
            except socket.error:
                break
        self.disconnect()

    def _recvall(self, n):
        # Helper function to receive n bytes or return None if EOF is hit
        data = bytearray()
        while len(data) < n:
            packet = self.socket.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

    def _process_received_data(self, data):
        # Process the received data from the device
        try:
            # TODO: we need to handle different types of messages from the device Firmware, App, Client, etc.
            firmware_message = firmware_pb2.FirmwareMessage()
            firmware_message.ParseFromString(data)
            # Handle different types of firmware messages
            if firmware_message.HasField('system_info'):
                self._handle_system_info(firmware_message.system_info)
            elif firmware_message.HasField('error'):
                self._handle_error(firmware_message.error)
            # Add other message types as needed
            
            # TODO: we need to handle different types of messages from the device Firmware, App, Client, etc.
            # Try parsing as AppResponse
            app_response = app_pb2.AppResponse()
            app_response.ParseFromString(data)

            if app_response.HasField('initial_response'):
                self._handle_initial_response(app_response.initial_response)
            elif app_response.HasField('token_response'):
                self._handle_token_response(app_response.token_response)
            elif app_response.HasField('user_request'):
                self._handle_user_response(app_response.user_request)
            else:
                print("Received unknown AppResponse.")
        except Exception as e:
            print(f"Failed to process AppResponse: {e}")
            # Fallback to existing handling or log the error

    def _handle_initial_response(self, initial_response: app_pb2.InitialResponse):
        print(f"Received initial response: {initial_response.args}")

    def _handle_token_response(self, token_response: app_pb2.TokenResponse):
        print(f"Received token: {token_response.token}")
        if token_response.finish_reason != app_pb2.TokenResponse.FINISH_REASON_UNSPECIFIED:
            finish_reason = app_pb2.TokenResponse.FinishReason.Name(token_response.finish_reason)
            print(f"Finish reason: {finish_reason}")

    def _handle_user_response(self, user_response: app_pb2.UserResponse):
        print(f"Received user response: {user_response.response}")

    def send_generate_request(self, prompt: str, request_id: str, **kwargs):
        """
        Send a GenerateRequest to the Truffle app.

        :param prompt: The prompt to send.
        :param request_id: A unique identifier for the request.
        :param kwargs: Additional optional parameters like max_tokens, temperature, etc.
        """
        if not self.connected:
            raise ConnectionError("Not connected to Truffle device.")

        generate_request = app_pb2.GenerateRequest()
        generate_request.id = request_id
        generate_request.prompt = prompt

        # Set optional parameters if provided
        if 'max_tokens' in kwargs:
            generate_request.max_tokens = kwargs['max_tokens']

        if 'frequency_penalty' in kwargs:
            generate_request.frequency_penalty = kwargs['frequency_penalty']

        if 'presence_penalty' in kwargs:
            generate_request.presence_penalty = kwargs['presence_penalty']

        if 'temperature' in kwargs:
            generate_request.temperature = kwargs['temperature']

        if 'top_p' in kwargs:
            generate_request.top_p = kwargs['top_p']

        if 'response_format' in kwargs:
            generate_request.response_format = kwargs['response_format']

        if 'response_schema' in kwargs:
            generate_request.response_schema = kwargs['response_schema']

        if 'stop_strings' in kwargs:
            generate_request.stop_strings = kwargs['stop_strings']

        if 'stream' in kwargs:
            stream = generate_request.stream
            stream.content_type = kwargs['stream'].get('content_type')
            stream.additional_content = kwargs['stream'].get('additional_content', '')

        app_request = app_pb2.AppRequest()
        app_request.generate_request.CopyFrom(generate_request)

        self._send_app_request(app_request)

    def _send_app_request(self, app_request: app_pb2.AppRequest):
        data = app_request.SerializeToString()
        # Prepend the message length for framing
        msg_length = len(data).to_bytes(4, byteorder='big')
        self.socket.sendall(msg_length + data)

    def _handle_system_info(self, system_info):
        # Handle system info message
        print(f"Received system info: {system_info}")

    def _handle_error(self, error):
        # Handle error message
        print(f"Error from device: {error}")
  