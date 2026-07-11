from rich.console import Console, Group
from rich.panel import Panel

console = Console()

lab_test: list[str] = [
    "##### ###",
    "##    ###",
    "## ## ###",
    "##       ",
    "######## ",
    "         ",
]

to_display: list[str] = []
for line in lab_test:
    tmp: str = line.replace("#", "[purple]██")
    tmp = tmp.replace(" ", "[orchid]██")
    to_display.append(tmp)

final_lab = Group(*to_display)

my_panel = Panel(final_lab, expand=False, border_style="purple")
console.print(my_panel)
