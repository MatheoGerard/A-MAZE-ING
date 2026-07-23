from .wall_destroyer import change_state
from classes import Cells
import random


def check_back(cells_list: list[Cells], cell: Cells, size_values: list[int]) -> bool:
    change_line: int = (size_values[0] * 2) - 1

    if (
        cells_list[cell.index_list + 1].is_used
        and cells_list[cell.index_list - 1].is_used
        and cells_list[cell.index_list + change_line].is_used
        and cells_list[cell.index_list - change_line].is_used
    ):
        return True

    return False


def back_track(
    cells_list: list[Cells],
    cell: Cells,
    direction_history: list[str],
    size_values: list[int],
) -> Cells:
    change_line: int = (size_values[0] * 2) - 1
    current_cell: Cells = cell

    while check_back(cells_list, cell, size_values):
        if direction_history.pop() == "N":
            current_cell = cells_list[cell.index_list - change_line]
        elif direction_history.pop() == "S":
            current_cell = cells_list[cell.index_list + change_line]
        elif direction_history.pop() == "E":
            current_cell = cells_list[cell.index_list + 1]
        else:
            current_cell = cells_list[cell.index_list - 1]

    return current_cell


def choice_direction(cell: Cells) -> str:
    is_ok: bool = False
    dir: str = ""

    while not is_ok:
        dir_list: list[str] = ["N", "W", "S", "E"]
        dir: str = dir_list[random.randint(0, len(dir_list) - 1)]
        if not cell.walls[dir]:
            continue
        is_ok = True

    return dir


def change_cell_state(
    cell: Cells,
    dir: str,
    size_values: list[int],
    cells_list: list[Cells],
    lab_lst: list[str],
) -> None:
    change_line: int = (size_values[0] * 2) - 1

    if dir == "N":
        cells_list[cell.index_list - change_line].char = " "
        lab_lst[cell.index_str - change_line - 1] = " "
    elif dir == "E":
        cells_list[cell.index_list + 1].char = " "
        lab_lst[cell.index_str + 1] = " "
    elif dir == "S":
        cells_list[cell.index_list - change_line].char = " "
        lab_lst[cell.index_str + change_line + 3] = " "
    elif dir == "W":
        cells_list[cell.index_list - 1].char = " "
        lab_lst[cell.index_str - 1] = " "


def change_current_cell(
    cell: Cells, cells_list: list[Cells], size_values: list[int], dir: str
) -> Cells:
    change_line: int = (size_values[0] * 2) - 1

    if dir == "N":
        return cells_list[cell.index_list - (change_line * 2)]
    elif dir == "E":
        return cells_list[cell.index_list + 2]
    elif dir == "S":
        return cells_list[cell.index_list + (change_line * 2)]
    else:
        return cells_list[cell.index_list - 2]


def gen_maze(
    cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> None:
    current: Cells = cells_list[0]
    direction_history: list[str] = []

    direction: str = choice_direction(current)
    direction_history.append(direction)

    change_cell_state(current, direction, size_values, cells_list, lab_lst)
    current = change_current_cell(current, cells_list, size_values, direction)
