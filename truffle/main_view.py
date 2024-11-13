import typer
from truffle_client import TruffleClient

class MainView:
    def __init__(self):
        self.truffle_client = TruffleClient()
        self.connected = False

    def start(self):
        typer.echo("Connecting to Truffle device...")
        # Replace with actual logic to retrieve the magic code
        magic_code = "1234"
        truffle_host = f"truffle-{magic_code}.local"
        try:
            self.truffle_client.connect(truffle_host)
            self.connected = True
            typer.echo("Connected to Truffle device.")
            self.main_menu()
        except Exception as e:
            typer.echo(f"Failed to connect: {e}")

    def main_menu(self):
        while self.connected:
            typer.echo("\nMain Menu:")
            typer.echo("1. Send Prompt")
            typer.echo("2. Get Info")
            typer.echo("3. Exit")
            choice = typer.prompt("Enter your choice")
            if choice == "1":
                self.send_prompt()
            elif choice == "2":
                self.get_info()
            elif choice == "3":
                self.connected = False
                self.truffle_client.disconnect()
            else:
                typer.echo("Invalid choice.")

    def send_prompt(self):
        message = typer.prompt("Enter your message")
        prompt = client_pb2.Prompt()
        prompt.prompt_id = "prompt-1"
        prompt.message = message
        client_message = client_pb2.ClientMessage()
        client_message.prompt.CopyFrom(prompt)
        self.truffle_client._send_message(client_message)
        typer.echo("Prompt sent.")

    def get_info(self):
        info = client_pb2.Info()
        info.truffle_id = "client-1"
        client_message = client_pb2.ClientMessage()
        client_message.info.CopyFrom(info)
        self.truffle_client._send_message(client_message)
        typer.echo("Info request sent.") 