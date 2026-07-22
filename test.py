from rich.console import Console
from rich.panel import Panel
import parsing
from classes import Cells
from typing import Any
import algo

console = Console()


def input_panel() -> None:
    inputs: str = "Change color: 0\nRegenerate maze: \nExit: 9"
    input_panel = Panel(inputs, expand=False, border_style="green")
    console.print(input_panel)


def visualizatoin_format(to_display: str, color_set: str) -> None:
    colors: list[str] = color_set.split("-")
    tmp: str = to_display.replace("#", f"[{colors[0]}]██")
    tmp2: str = tmp.replace(".", f"[{colors[2]}]██")
    tmp3: str = tmp2.replace("E", "[green]██")
    tmp4: str = tmp3.replace("L", "[red]██")
    final = tmp4.replace(" ", f"[{colors[1]}]██")
    my_panel = Panel(final, expand=False, border_style="purple")
    console.print(my_panel)


def draw_lab_size(
    size: list[int], entry_val: list[int], exit_val: list[int]
) -> tuple[str, list[Cells]]:
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
                    new_cell: Cells = Cells(True, len(buffer), j, x - 1, size)
                    if new_cell.position == entry_val or new_cell.position == exit_val:
                        print(new_cell.position)
                        new_cell.char = "E"
                    cells_list.append(new_cell)
                    buffer += new_cell.char
            else:
                for y in range_width:
                    if y == width_total - 1:
                        buffer += "."
                        break
                    if y % 2 != 0:
                        new_cell: Cells = Cells(True, len(buffer), y, x - 1, size)
                        if (
                            new_cell.position == entry_val
                            or new_cell.position == exit_val
                        ):
                            print(new_cell.position)
                            new_cell.char = "E"
                        cells_list.append(new_cell)
                        buffer += new_cell.char
                    else:
                        new_cell: Cells = Cells(False, len(buffer), y, x - 1, size)
                        if (
                            new_cell.position == entry_val
                            or new_cell.position == exit_val
                        ):
                            print(new_cell.position)
                            new_cell.char = "E"
                        cells_list.append(new_cell)
                        buffer += new_cell.char

            buffer += "\n"
        is_finish = True

    return (buffer, cells_list)


def set_cells_index(cells_list: list[Cells]) -> None:
    index: int = 0

    for c in cells_list:
        c.index_list = index
        index += 1


def entry_exit_in_symbol(entry_exit: list[list[int]], cells_list: list[Cells]) -> None:
    for c in cells_list:
        if c.position == entry_exit[0]:
            raise ValueError("Entry in middle symbol")
        elif c.position == entry_exit[1]:
            raise ValueError("Exit in middle symbol")


def init_lab(index: int, color_set: list[str]) -> None:
    parse_data: dict[str, Any] = parsing.parsing_config("config.txt")
    parsing.validate_config(parse_data)
    size_values: list[int] = parsing.validate_size_value(parse_data)
    entry_exit: list[list[int]] = parsing.validate_entry_exit(parse_data, size_values)
    parsing.validate_perfect(parse_data)
    parsing.validate_output_name(parse_data)
    console.clear()
    lab_data: tuple[str, list[Cells]] = draw_lab_size(
        size_values, entry_exit[0], entry_exit[1]
    )
    lab_data_str: str = lab_data[0]
    active_cell: list[Cells] = lab_data[1]
    set_cells_index(active_cell)
    lab_data_lst: list[str] = list(lab_data_str)
    symbol_lst: list[Cells] = algo.symbol_logic(active_cell, size_values, lab_data_lst)
    # for c in active_cell:
    #   if not c.char == "#":
    #      print(c.position)
    #     print(c.walls)
    print(algo.gen_maze(active_cell))
    entry_exit_in_symbol(entry_exit, symbol_lst)
    visualizatoin_format("".join(lab_data_lst), color_set[index])
    input_panel()


def loop_gameplay() -> None:
    color_set: list[str] = [
        "dark_red-dark_goldenrod-dark_orange3",
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
    try:
        loop_gameplay()
    except ValueError as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)
