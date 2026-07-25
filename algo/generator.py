from abc import abstractproperty
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
            and cells_list[cell.index_list + change_line * 2].is_used
        ):
            return True
    elif cell.position[1] == 0 and cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list + change_line * 2].is_used
        ):
            return True
    elif cell.position[1] == vertical_size and cell.position[0] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
        ):
            return True
    elif cell.position[1] == vertical_size and cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
        ):
            return True
    # NOTE: haut/bas
    elif cell.position[1] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list + change_line * 2].is_used
        ):
            return True
    elif cell.position[1] == vertical_size:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
        ):
            return True
    # NOTE: droite/gauche
    elif cell.position[0] == 0:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
            and cells_list[cell.index_list + change_line * 2].is_used
        ):
            return True
    elif cell.position[0] == change_line:
        if (
            cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
            and cells_list[cell.index_list + change_line * 2].is_used
        ):
            return True
    # NOTE: normal
    else:
        if (
            cells_list[cell.index_list + 2].is_used
            and cells_list[cell.index_list - 2].is_used
            and cells_list[cell.index_list + change_line * 2].is_used
            and cells_list[cell.index_list - change_line * 2].is_used
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
    last_dir: str = ""

    while not choice_direction(cells_list, current_cell, size_values):
        if len(direction_history) == 0:
            break

        last_dir = direction_history.pop()

        if last_dir == "N":
            current_cell = cells_list[current_cell.index_list + change_line * 2]
        elif last_dir == "S":
            current_cell = cells_list[current_cell.index_list - change_line * 2]
        elif last_dir == "E":
            current_cell = cells_list[current_cell.index_list - 2]
        elif last_dir == "W":
            current_cell = cells_list[current_cell.index_list + 2]

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
    cells_list: list[Cells],
    cell: Cells,
    size_values: list[int],
) -> str:
    dir: str = ""
    dir_list: list[str] = []

    change_line: int = (size_values[0] * 2) - 1

    dir_list = ["N", "E", "S", "W"]

    if not cell.walls["N"]:
        dir_list.remove("N")
    if not cell.walls["S"]:
        dir_list.remove("S")
    if not cell.walls["E"]:
        dir_list.remove("E")
    if not cell.walls["W"]:
        dir_list.remove("W")

        # for dir in dir_list:
        # if len(direction_history) != 0 and dir == direction_history[-1]:
        #   dir_list.remove(reverse_dict[dir])

    if "N" in dir_list:
        if cells_list[cell.index_list - change_line * 2].is_used:
            dir_list.remove("N")

    if "S" in dir_list:
        if cells_list[cell.index_list + change_line * 2].is_used:
            dir_list.remove("S")

    if "E" in dir_list:
        if cells_list[cell.index_list + 2].is_used:
            dir_list.remove("E")

    if "W" in dir_list:
        if cells_list[cell.index_list - 2].is_used:
            dir_list.remove("W")

    if len(dir_list) == 0:
        return ""
    else:
        dir: str = random.choice(dir_list)

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
        cells_list[cell.index_list - (change_line)].char = " "
        lab_lst[cell.index_str - change_line - 3] = " "
    elif dir == "E":
        cells_list[cell.index_list + 1].char = " "
        lab_lst[cell.index_str + 1] = " "
    elif dir == "S":
        cells_list[cell.index_list + (change_line)].char = " "
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


def check_north(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> bool:
    if not current.walls["N"]:
        return False

    change_line: int = (size_values[0] * 2) - 1

    if cells_list[current.index_list - (change_line * 2)].char == " ":
        return True

    return False


def check_south(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> bool:
    if not current.walls["S"]:
        return False

    change_line: int = (size_values[0] * 2) - 1

    if cells_list[current.index_list + (change_line * 2)].char == " ":
        return True

    return False


def check_east(current: Cells, cells_list: list[Cells]) -> bool:
    if not current.walls["E"]:
        return False

    if cells_list[current.index_list + 2].char == " ":
        return True

    return False


def check_west(current: Cells, cells_list: list[Cells]) -> bool:
    if not current.walls["W"]:
        return False

    if cells_list[current.index_list - 2].char == " ":
        return True

    return False


def check_dead_ends(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> tuple[bool, str | None]:
    nb_direction: list[str] = []
    change_line: int = (size_values[0] * 2) - 1

    if (
        current.position[0] != (size_values[0] * 2) - 2
        and cells_list[current.index_list + 1].char == " "
    ):
        nb_direction.append("E")

    if current.position[0] != 0 and cells_list[current.index_list - 1].char == " ":
        nb_direction.append("W")

    if (
        current.position[1] != (size_values[1] * 2) - 2
        and cells_list[current.index_list + change_line].char == " "
    ):
        nb_direction.append("S")

    if (
        current.position[1] != 0
        and cells_list[current.index_list - change_line].char == " "
    ):
        nb_direction.append("N")

    if len(nb_direction) == 1:
        return (True, nb_direction[0])

    return (False, None)


def destroy_dead_ends(
    current: Cells, cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> None:
    list_direction: list[str] = []
    check: tuple[bool, str | None] = check_dead_ends(current, cells_list, size_values)
    change_line: int = (size_values[0] * 2) - 1

    if check[0]:
        if check_north(current, cells_list, size_values):
            list_direction.append("N")
        if check_south(current, cells_list, size_values):
            list_direction.append("S")
        if check_east(current, cells_list):
            list_direction.append("E")
        if check_west(current, cells_list):
            list_direction.append("W")

    if len(list_direction) > 0:
        direction_to_go: str = random.choice(list_direction)

        if direction_to_go == "N":
            cells_list[current.index_list - change_line].char = " "
            lab_lst[current.index_str - change_line - 3] = " "
        if direction_to_go == "S":
            cells_list[current.index_list + change_line].char = " "
            lab_lst[current.index_str + change_line + 3] = " "
        if direction_to_go == "W":
            cells_list[current.index_list - 1].char = " "
            lab_lst[current.index_str - 1] = " "
        if direction_to_go == "E":
            cells_list[current.index_list + 1].char = " "
            lab_lst[current.index_str + 1] = " "


def unperfect(
    cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> None:
    change_line: int = (size_values[0] * 2) - 2
    for c in cells_list:
        if c.char == " ":
            destroy_dead_ends(c, cells_list, size_values, lab_lst)


def gen_maze(
    cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> list[str]:
    current: Cells = cells_list[0]
    direction_history: list[str] = []
    current.is_used = True

    while not finish_check(cells_list):
        direction: str = choice_direction(cells_list, current, size_values)
        if not direction:
            current = back_track(cells_list, current, direction_history, size_values)
            if len(direction_history) == 0:
                break
            continue
        direction_history.append(direction)
        change_cell_state(current, direction, size_values, cells_list, lab_lst)
        current = change_current_cell(current, cells_list, size_values, direction)
        current.is_used = True
        debug_number_cells(cells_list)
    return lab_lst
