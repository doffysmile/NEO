from rich.table import Table
from rich.rule import Rule
from rich.text import Text

from neo.ui.console import console


def render_system_info(data: dict) -> None:

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        expand=False
    )

    table.add_column(style="neo.primary", min_width=12)
    table.add_column(style="neo.secondary")
    table.add_column(style="neo.info")

    table.add_row("HOST", ":", Text(data["host"]))
    table.add_row("OS", ":", Text(data["os"]))
    table.add_row("KERNEL", ":", Text(data["kernel"]))
    table.add_row("ARCH", ":", Text(data["arch"]))
    table.add_row("USER", ":", Text(data["user"]))
    table.add_row("INTERFACE", ":", Text(data["interface"]))
    table.add_row("CPU", ":", Text(data["cpu"]))

    table.add_row(
        "MEMORY",
        ":",
        f'{data["memory_total"]:.2f} GiB (total)'
    )

    console.print()
    console.print("SYSTEM INFORMATION", style="neo.primary")
    console.print(Rule(style="neo.secondary"))
    console.print(table)
    console.print(Rule(style="neo.secondary"))
    console.print()