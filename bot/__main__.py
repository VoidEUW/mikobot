"""MikoBot (c) 2024-2025 by Void"""

from sys import argv

from bot.events import event_listener
from bot.miko import MikoBot


def main():
    """Main entry point for the MikoBot application."""
    client = MikoBot()

    event_listener(client)

    client.run(get_token(), root_logger=True)


def get_token() -> str:
    """Get the token from the command line arguments."""
    if len(argv) < 2:
        print("Usage: python -m bot <token>")
        exit(1)
    elif argv[1] == "":
        print("Error: You must provide a token.")
        exit(1)
    return str(argv[1])


if __name__ == "__main__":
    main()
