
from neo.ui.console import console
from rich.rule import Rule
from rich.text import Text


def startup():
    banner = Text(
        """
│   Wake up, Neo...                                            │
│   The Matrix has you...                                      │
│   Follow the white rabbit.                                   │
│                                                              │
│   1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 0 1                    │
│   0 1 1 0 1 0 0 1 1 0 1 0 1 1 0 0 1 0 1 1                    │
│   1 1 0 0 1 1 0 1 0 1 1 0 0 1 1 0 1 0 0 1
""",
        style="neo.primary"
    )

    console.print(banner)
    console.print("NEO // DEVELOPMENT BUILD",
                  style="neo.secondary")

    console.print(Rule(style="neo.secondary"))

    console.print("Wake up.", style="neo.primary")
    console.print("Interface initialized.", style="neo.info")
    console.print("Type 'help' for commands.\n",
                  style="neo.muted")
