from .wall_destroyer import change_state
from classes import Cells
import random


def check_back(cells_list: list[Cells], cell: Cells, size_values: list[int]) -> bool:
    change_line: int = (size_values[0] * 2) - 2
    vertical_size: int = (size_values[1] * 2) - 2

    # NOTE: corners
    if cell.position[1] == 0 and cell.position[0] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list + change_line].is_used
        ):
            return True
    elif cell.position[1] == 0 and cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list + change_line].is_used
        ):
            return True
    elif cell.position[1] == vertical_size and cell.position[0] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - change_line].is_used
        ):
            return True
    elif cell.position[1] == vertical_size and cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line].is_used
        ):
            return True
    # NOTE: haut/bas
    elif cell.position[1] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list + change_line].is_used
        ):
            return True
    elif cell.position[1] == vertical_size:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line].is_used
        ):
            return True
    # NOTE: droite/gauche
    elif cell.position[0] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - change_line].is_used
            and cells_list[cell.index_list + change_line].is_used
        ):
            return True
    elif cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line].is_used
            and cells_list[cell.index_list + change_line].is_used
        ):
            return True
    # NOTE: normal
    else:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
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
    change_line: int = (size_values[0] * 2) - 2
    current_cell: Cells = cell

    while check_back(cells_list, current_cell, size_values):
        print(current_cell.position)
        if len(direction_history) == 0:
            print("no direction in history")
            break
        if direction_history[-1] == "N":
            direction_history.pop()
            current_cell = cells_list[cell.index_list + change_line]
        elif direction_history[-1] == "S":
            direction_history.pop()
            current_cell = cells_list[cell.index_list - change_line]
        elif direction_history[-1] == "E":
            direction_history.pop()
            current_cell = cells_list[cell.index_list - 2]
        elif direction_history[-1] == "W":
            direction_history.pop()
            current_cell = cells_list[cell.index_list + 2]

    return current_cell


def debug_number_cells(cell_list: list[Cells]):
    nb_cell: int = 0
    active_cells: list[Cells] = []

    for c in cell_list:
        if c.position[0] % 2 == 0 and c.position[1] % 2 == 0:
            active_cells.append(c)
    for c in active_cells:
        if c.is_used:
            nb_cell += 1

    total_cell: int = len(active_cells)
    # print(f"{total_cell} vs {nb_cell}")


def choice_direction(
    reverse_dict: dict[str, str],
    cells_list: list[Cells],
    cell: Cells,
    direction_history: list[str],
    size_values: list[int],
) -> str:
    dir: str = ""
    dir_list: list[str] = []

    change_line: int = (size_values[0] * 2) - 2

    dir_list = ["N", "E", "S", "W"]

    for dir in dir_list:
        if not cell.walls[dir]:
            print(f"remove {dir} to cell:{cell.index_list}")
            dir_list.remove(dir)

    for dir in dir_list:
        if len(direction_history) != 0 and dir == direction_history[-1]:
            dir_list.remove(reverse_dict[dir])

    if "N" in dir_list:
        if cells_list[cell.index_list - change_line].is_used:
            dir_list.remove("N")

    if "S" in dir_list:
        if cells_list[cell.index_list + change_line].is_used:
            dir_list.remove("S")

    if "E" in dir_list:
        if cells_list[cell.index_list + 2].is_used:
            dir_list.remove("E")

    if "W" in dir_list:
        if cells_list[cell.index_list - 2].is_used:
            dir_list.remove("W")

    dir: str = dir_list[random.randint(0, len(dir_list) - 1)]

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
        lab_lst[cell.index_str - change_line - 3] = " "
    elif dir == "E":
        cells_list[cell.index_list + 1].char = " "
        lab_lst[cell.index_str + 1] = " "
    elif dir == "S":
        cells_list[cell.index_list - change_line].char = " "
        lab_lst[cell.index_str + change_line + 3] = " "
    elif dir == "W":
        cells_list[cell.index_list - 1].char = " "
        lab_lst[cell.index_str - 1] = " "


def finish_check(cell_list: list[Cells]):
    for c in cell_list:
        if c.position[0] % 2 == 0 and c.position[1] % 2 == 0:
            if not c.is_used:
                return False

    return True


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
    current.is_used = True
    direction_reverse: dict[str, str] = {"N": "S", "S": "N", "E": "W", "W": "E"}

    while not finish_check(cells_list):
        back_track(cells_list, current, direction_history, size_values)
        direction: str = choice_direction(
            direction_reverse, cells_list, current, direction_history, size_values
        )
        direction_history.append(direction)
        change_cell_state(current, direction, size_values, cells_list, lab_lst)
        current = change_current_cell(current, cells_list, size_values, direction)
        current.is_used = True
        debug_number_cells(cells_list)
