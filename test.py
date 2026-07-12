from rich.console import Console
from rich.panel import Panel
import parsing
from classes import Cells

console = Console()

lab_test: list[str] = [
    "##### ###",
    "##    ###",
    "## ## ###",
    "##       ",
    "######## ",
    "         ",
]


def input_panel() -> None:
    inputs: str = "Change color: 0\nRegenerate maze: \nExit: 9"
    input_panel = Panel(inputs, expand=False, border_style="green")
    console.print(input_panel)


def change_colors() -> None:
    color_set: list[str] = ["purple-orchid-blue", "bright_red-grey0-bright_blue"]


def visualizatoin_format(to_display: str, color_set: str) -> None:
    colors: list[str] = color_set.split("-")
    tmp: str = to_display.replace("#", f"[{colors[0]}]██")
    tmp: str = tmp.replace(".", f"[{colors[2]}]██")
    final = tmp.replace(" ", f"[{colors[1]}]██")
    my_panel = Panel(final, expand=False, border_style="purple")
    console.print(my_panel)


def draw_lab_size(size: list[int]) -> str:
    cells_list: list[Cells] = []
    buffer: str = ""
    width_total: int = size[0] * 2
    height_total: int = (size[1] * 2) + 2

    range_width = range(0, width_total)
    range_height = range(0, height_total - 1)

    is_finish: bool = False

    while not is_finish:
        for x in range_height:
            buffer += "."
            if x == 0:
                for _ in range_width:
                    buffer += "."
                buffer += "\n"
                continue

            if x == height_total - 2:
                for _ in range_width:
                    buffer += "."
                buffer += "\n"
                continue

            if x % 2 == 0:
                for j in range_width:
                    if j == width_total - 1:
                        buffer += "."
                        break
                    new_cell: Cells = Cells(True, j, x - 1)
                    cells_list.append(new_cell)
                    buffer += new_cell.char
            else:
                for y in range_width:
                    if y == width_total - 1:
                        buffer += "."
                        break
                    if y % 2 != 0:
                        new_cell: Cells = Cells(True, y, x - 1)
                        cells_list.append(new_cell)
                        buffer += new_cell.char
                    else:
                        new_cell: Cells = Cells(False, y, x - 1)
                        cells_list.append(new_cell)
                        buffer += new_cell.char

            buffer += "\n"
        is_finish = True

    return buffer


def init_lab(index: int, color_set: list[str]) -> None:
    console.clear()
    size: list[int] = parsing.ps("config.txt")
    display: str = draw_lab_size(size)
    visualizatoin_format(display, color_set[index])
    input_panel()


def loop_gameplay() -> None:
    color_set: list[str] = [
        "purple-orchid-blue",
        "bright_red-grey0-bright_blue",
        "grey3-grey46-grey85",
    ]

    is_exit: bool = False
    color_index: int = 0

    init_lab(color_index, color_set)
    while not is_exit:
        key: str = input("Input: ")
        match key:
            case "9":
                is_exit = True
                print("Exit...")
            case "0":
                if color_index == len(color_set) - 1:
                    color_index = 0
                else:
                    color_index += 1
                init_lab(color_index, color_set)
            case _:
                print("This choice is not supported!")


if __name__ == "__main__":
    loop_gameplay()
