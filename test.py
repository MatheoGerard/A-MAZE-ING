from rich.console import Console, Group
from rich.panel import Panel
import parsing

console = Console()

lab_test: list[str] = [
    "##### ###",
    "##    ###",
    "## ## ###",
    "##       ",
    "######## ",
    "         ",
]


def visualizatoin_format(to_display: str) -> None:
    tmp: str = to_display.replace("#", "[purple]██")
    final = tmp.replace(" ", "[orchid]██")
    my_panel = Panel(final, expand=False, border_style="purple")
    console.print(my_panel)


def draw_lab_size(size: list[int]) -> str:
    buffer: str = ""
    is_wall: bool = True
    for loop in range(0, size[1]):
        for _ in range(0, size[0]):
            if is_wall:
                buffer = buffer + "#"
                is_wall = False
            else:
                buffer = buffer + " "
                is_wall = True
        if not loop == size[1] - 1:
            buffer += "\n"
    return buffer


if __name__ == "__main__":
    try:
        size: list[int] = parsing.ps("config.txt")
        display: str = draw_lab_size(size)
        visualizatoin_format(display)
    except Exception as e:
        print(e)
