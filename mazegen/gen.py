from .parsing_config import validate_config, validate_entry_exit, validate_output_name, validate_perfect, validate_size_value, seed_parsing
from typing import Any
import random
from .generator import unperfect
from .print42 import symbol_logic
from .generator import gen_maze
from .hex_traductor import hex_trad
from .cells_class import Cells
from .bfs_solver import bfs_function


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
                    if new_cell.position == entry_val:
                        new_cell.char = "E"
                        new_cell.is_entry = True
                    elif new_cell.position == exit_val:
                        new_cell.char = "e"
                        new_cell.is_exit = True
                    cells_list.append(new_cell)
                    buffer += new_cell.char
            else:
                for y in range_width:
                    if y == width_total - 1:
                        buffer += "."
                        break
                    if y % 2 != 0:
                        new_cell = Cells(True, len(buffer), y, x - 1, size)
                        if new_cell.position == entry_val:
                            new_cell.char = "E"
                            new_cell.is_entry = True
                        elif new_cell.position == exit_val:
                            new_cell.char = "e"
                            new_cell.is_exit = True
                        cells_list.append(new_cell)
                        buffer += new_cell.char
                    else:
                        new_cell = Cells(False, len(buffer), y, x - 1, size)
                        if new_cell.position == entry_val:
                            new_cell.char = "E"
                            new_cell.is_entry = True
                        elif new_cell.position == exit_val:
                            new_cell.char = "e"
                            new_cell.is_exit = True
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


def entry_exit_in_symbol(
    entry_exit: list[list[int]], cells_list: list[Cells]
) -> None:
    for c in cells_list:
        if c.position == entry_exit[0]:
            raise ValueError("Entry in middle symbol")
        elif c.position == entry_exit[1]:
            raise ValueError("Exit in middle symbol")


def init_lab(
    symbol_index: int,
    parse_data: dict[str, Any],
) -> tuple[list[str], list[Cells | str], list[Cells], list[int]]:
    validate_config(parse_data)
    size_values: list[int] = validate_size_value(parse_data)
    entry_exit: list[list[int]] = validate_entry_exit(
        parse_data, size_values
    )
    perfect: bool = validate_perfect(parse_data)
    validate_output_name(parse_data)
    seed: None | str = seed_parsing(parse_data)
    if seed:
        random.seed(seed)
    lab_data: tuple[str, list[Cells]] = draw_lab_size(
        size_values, entry_exit[0], entry_exit[1]
    )
    lab_data_str: str = lab_data[0]
    active_cell: list[Cells] = lab_data[1]
    set_cells_index(active_cell)
    lab_data_lst: list[str] = list(lab_data_str)
    if size_values[0] > 8 and size_values[1] > 6:
        symbol_lst: list[Cells] = symbol_logic(
            active_cell, size_values, lab_data_lst, symbol_index
        )
    else:
        print("[red]Not enough space for 42 symbol![/red]")
    lab_data_lst = gen_maze(active_cell, size_values, lab_data_lst)
    if not perfect:
        unperfect(active_cell, size_values, lab_data_lst)
    soluce: list[Cells | str] = bfs_function(active_cell, size_values)
    hex_trad(
        active_cell,
        size_values,
        parse_data["OUTPUT_FILE"],
        parse_data["ENTRY"],
        parse_data["EXIT"],
        soluce,
    )
    if size_values[0] > 8 and size_values[1] > 6:
        entry_exit_in_symbol(entry_exit, symbol_lst)

    return lab_data_lst, soluce, active_cell, size_values
