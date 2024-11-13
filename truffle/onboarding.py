import time
import typer
from network_manager import NetworkManager
from truffle_client import TruffleClient
from getpass import getpass
from typing import Optional
import json
import os

class OnboardingCache:
    CACHE_FILE = os.path.expanduser("~/.truffle_onboarding.json")

    @staticmethod
    def save_onboarding_state(state: dict):
        with open(OnboardingCache.CACHE_FILE, 'w') as f:
            json.dump(state, f)

    @staticmethod
    def load_onboarding_state() -> dict:
        if os.path.exists(OnboardingCache.CACHE_FILE):
            with open(OnboardingCache.CACHE_FILE, 'r') as f:
                return json.load(f)
        return {}

class OnboardingView:
    def __init__(self):
        self.network_manager = NetworkManager()
        self.truffle_client = TruffleClient()
        self.magic_code = ""  # Should be provided by the user
        self.main_ssid = ""    # Main Wi-Fi SSID
        self.main_password = ""  # Main Wi-Fi password
        self.truffle_name = ""  # Name to assign to the Truffle device
        self.truffle_host = ""  # Hostname of the Truffle device on LAN

    def start(self):
        typer.echo("Starting onboarding process...")

        # Step 1: Get the magic code
        self.magic_code = typer.prompt("Enter your magic code")
        hotspot_ssid = f"truffle-{self.magic_code[-4:]}"
        hotspot_password = hotspot_ssid
        self.truffle_host = f"truffle-{self.magic_code[-4:]}.local"

        # Step 2: Connect to the Truffle hotspot
        typer.echo(f"Connecting to Truffle hotspot {hotspot_ssid}...")
        self.network_manager.connect_to_wifi(hotspot_ssid, hotspot_password)
        time.sleep(5)  # Wait for the connection to establish

        # Step 3: Get main Wi-Fi credentials
        self.main_ssid = typer.prompt("Enter your main Wi-Fi SSID")
        self.main_password = getpass("Enter your main Wi-Fi Password")

        # Step 4: (Optional) Get the desired name for the Truffle device
        self.truffle_name = typer.prompt("Enter a name for your Truffle device", default="MyTruffle")

        # Step 5: Send Wi-Fi credentials to Truffle device
        typer.echo("Connecting to Truffle device over hotspot...")
        try:
            self.truffle_client.connect("192.168.4.1")  # Common IP for devices in AP mode
            typer.echo("Connected to Truffle device. Sending Wi-Fi credentials...")
            self.truffle_client.send_wifi_credentials(self.main_ssid, self.main_password, self.truffle_name)
            typer.echo("Credentials sent successfully.")
        except Exception as e:
            typer.echo(f"Failed to send credentials to Truffle device: {e}")
            self.cleanup()
            return

        self.truffle_client.disconnect()
        time.sleep(2)

        # Step 6: Reconnect to main Wi-Fi
        typer.echo("Reconnecting to main Wi-Fi...")
        self.network_manager.connect_to_wifi(self.main_ssid, self.main_password)
        time.sleep(10)  # Give time for both the client and Truffle device to connect to the main Wi-Fi

        # Step 7: Wait for Truffle device on LAN
        typer.echo("Waiting for Truffle device to connect to LAN...")
        connected = False
        for attempt in range(15):
            if self.network_manager.ping_host(self.truffle_host):
                connected = True
                break
            typer.echo(f"Attempt {attempt + 1}/15: Truffle device not reachable yet. Retrying in 2 seconds...")
            time.sleep(2)

        if not connected:
            typer.echo("Failed to connect to Truffle device on LAN after multiple attempts.")
            self.cleanup()
            return

        typer.echo("Connected to Truffle device over LAN.")

        # Step 8: Verify settings (Optional)
        try:
            self.truffle_client.connect(self.truffle_host)
            typer.echo("Connected to Truffle device over LAN.")
            # You can request system info or verify settings here
            # Optionally, you can implement methods to fetch and display device settings
            self.truffle_client.disconnect()
        except Exception as e:
            typer.echo(f"Failed to connect to Truffle device over LAN: {e}")

        typer.echo("Onboarding completed successfully!")

        # Save onboarding state
        state = {
            'magic_code': self.magic_code,
            'main_ssid': self.main_ssid,
            'truffle_host': self.truffle_host
        }
        OnboardingCache.save_onboarding_state(state)

    def cleanup(self):
        # Optional cleanup method to reset network settings if needed
        self.truffle_client.disconnect()
        self.network_manager.connect_to_wifi(self.main_ssid, self.main_password)
 