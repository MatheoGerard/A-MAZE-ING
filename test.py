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


def visualizatoin_format(to_display: str) -> None:
    tmp: str = to_display.replace("#", "[purple]██")
    tmp: str = tmp.replace(".", "[blue]██")
    final = tmp.replace(" ", "[orchid]██")
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

    # FIXME: supp les debug
    debug_len: int = 0

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
                    print(new_cell.position)
                    cells_list.append(new_cell)
                    buffer += new_cell.char
            else:
                for y in range_width:
                    if y == width_total - 1:
                        buffer += "."
                        break
                    if y % 2 != 0:
                        new_cell: Cells = Cells(True, y, x - 1)
                        print(new_cell.position)
                        cells_list.append(new_cell)
                        buffer += new_cell.char
                    else:
                        new_cell: Cells = Cells(False, y, x - 1)
                        print(new_cell.position)
                        cells_list.append(new_cell)
                        buffer += new_cell.char

                        # FIXME: supp les debug
                        debug_len += 1

            buffer += "\n"
        is_finish = True

        # FIXME: supp les debug
        print(debug_len)
        print(len(cells_list))

    return buffer


if __name__ == "__main__":
    try:
        size: list[int] = parsing.ps("config.txt")
        display: str = draw_lab_size(size)
        visualizatoin_format(display)
    except Exception as e:
        print(e)
