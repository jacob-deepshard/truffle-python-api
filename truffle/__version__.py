from importlib.metadata import version

try:
    __version__ = version("truffle-cli")
except ImportError:
    # Package is not installed
    import os
    import tomli

    try:
        pyproject_path = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
        with open(pyproject_path, "rb") as f:
            pyproject = tomli.load(f)
            __version__ = pyproject["tool"]["poetry"]["version"]
    except (FileNotFoundError, KeyError, ImportError):
        __version__ = "unknown"
