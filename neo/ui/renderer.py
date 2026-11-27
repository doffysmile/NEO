
from rich.markdown import Markdown
from neo.ui.console import console


def render_response(response: str):
    console.print(Markdown(response))


def render_command(response: str):
    console.print(response, markup=False, highlight=False)


def render_error(message: str):
    console.print(
        message,
        style="neo.error",
        markup=False
    )
