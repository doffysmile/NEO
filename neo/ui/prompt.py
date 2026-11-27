from neo.ui.console import console


def get_input() -> str:
    return console.input(
        "[neo.prompt]NEO > [/neo.prompt]"
    ).strip()
