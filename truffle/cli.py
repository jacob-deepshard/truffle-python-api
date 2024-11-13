import typer
from onboarding import OnboardingView
from main_view import MainView

app = typer.Typer(
    name="truffle",
    help="Truffle CLI - Command line interface for TruffleOS",
    no_args_is_help=True,
)

@app.command()
def onboard():
    """Onboard a new Truffle device"""
    OnboardingView().start()

@app.command()
def run():
    """Run the main Truffle CLI"""
    MainView().start()

@app.command()
def version():
    """Show the current version of Truffle CLI"""
    typer.echo("Truffle CLI version 0.1.0") 