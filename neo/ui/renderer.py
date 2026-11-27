from rich.markdown import Markdown

from neo.ui.console import console
from neo.ui.views.system_view import render_system_info


def render_response(response: str) -> None:
    console.print(Markdown(response))


def render_command(response: str | dict) -> None:
    if isinstance(response, dict):
        render_system_info(response)

    else:
        console.print(
            response,
            markup=False,
            highlight=False
        )


def render_error(message: str) -> None:
    console.print(
        message,
        style="neo.error",
        markup=False
    )