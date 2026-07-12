from typing import Generator
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
    width_total: int = size[0] * 2
    height_total: int = (size[1] * 2) + 2

    range_width = range(0, width_total)
    range_height = range(0, height_total - 1)

    is_finish: bool = False

    while not is_finish:
        for x in range_height:
            buffer += "#"
            if x == 0:
                for _ in range_width:
                    buffer += "#"
                buffer += "\n"
                continue
            if x % 2 == 0:
                for _ in range_width:
                    buffer += "#"
            else:
                for y in range_width:
                    if y % 2 != 0:
                        buffer += "#"
                    else:
                        buffer += " "
            buffer += "\n"
        is_finish = True

    return buffer


if __name__ == "__main__":
    try:
        size: list[int] = parsing.ps("config.txt")
        display: str = draw_lab_size(size)
        visualizatoin_format(display)
    except Exception as e:
        print(e)
