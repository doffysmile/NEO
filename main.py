#!/usr/bin/env python3

from neo.commands import process_command
from neo.memory import save_memory
from neo.brain import ask_model

from neo.ui.boot import startup
from neo.ui.prompt import get_input
from neo.ui.renderer import (
    render_response,
    render_command,
    render_error,
)


def main():
    startup()

    while True:
        try:
            user_input = get_input()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                render_command("Goodbye!")
                break

            command_result = process_command(user_input)

            if command_result is not None:
                render_command(command_result)
            else:
                response = ask_model(user_input)
                render_response(response)

            save_memory(user_input)

        except (KeyboardInterrupt, EOFError):
            render_command("\nGoodbye!")
            break

        except Exception as error:
            render_error(f"Error: {error}")


if __name__ == "__main__":
    main()
