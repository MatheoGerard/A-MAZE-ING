from classes import Cells
from .wall_destroyer import change_state


def find_center(size_values: list[int]) -> tuple[int, int]:
    x_range: int = size_values[0] * 2
    x_center: int = int((x_range - 2) / 2)

    y_range: int = size_values[1] * 2
    y_center: int = int((y_range - 2) / 2)

    return (x_center, y_center)


def change_symbole(index: int, symbole_nb: int) -> int:
    if index == symbole_nb - 1:
        return 0
    else:
        return index + 1


def center_symbol(
    cells_list: list[Cells],
    center: tuple[int, int],
    size_values: list[int],
    lab_str: list[str],
    symbole_index: int,
) -> list[Cells]:
    cell_center: Cells = cells_list[0]
    change_line: int = (size_values[0] * 2) - 1
    list_symbole: list[list[Cells]] = []

    for c in cells_list:
        if c.position[0] == center[0] and c.position[1] == center[1]:
            cell_center = c
            break

    symbole_42: list[Cells] = [
        cells_list[cell_center.index_list - 1],
        cells_list[cell_center.index_list - 2],
        cells_list[cell_center.index_list - 3],
        cells_list[cell_center.index_list - 3 - change_line],
        cells_list[cell_center.index_list - 3 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list - 1 + (change_line * 2)],
        cells_list[cell_center.index_list + 1],
        cells_list[cell_center.index_list + 2],
        cells_list[cell_center.index_list + 3],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list + 1 + (change_line * 2)],
        cells_list[cell_center.index_list + 3 - change_line],
        cells_list[cell_center.index_list + 3 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 - (change_line * 2)],
        cells_list[cell_center.index_list + 1 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 3 + (change_line * 2)],
    ]
    list_symbole.append(symbole_42)

    symbole_invaders: list[Cells] = [
        cells_list[cell_center.index_list],
        cells_list[cell_center.index_list - 1],
        cells_list[cell_center.index_list - 2],
        cells_list[cell_center.index_list - 3],
        cells_list[cell_center.index_list - 4],
        cells_list[cell_center.index_list + 1],
        cells_list[cell_center.index_list + 2],
        cells_list[cell_center.index_list + 3],
        cells_list[cell_center.index_list + 4],
        cells_list[cell_center.index_list - change_line],
        cells_list[cell_center.index_list - 1 - change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list - 2 - change_line],
        cells_list[cell_center.index_list + 2 - change_line],
        cells_list[cell_center.index_list - 3 - change_line],
        cells_list[cell_center.index_list + 3 - change_line],
        cells_list[cell_center.index_list - (change_line * 2)],
        cells_list[cell_center.index_list + 1 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 2)],
        cells_list[cell_center.index_list - 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 - (change_line * 3)],
        cells_list[cell_center.index_list - 1 - (change_line * 4)],
        cells_list[cell_center.index_list + 1 - (change_line * 4)],
        cells_list[cell_center.index_list - 2 - (change_line * 4)],
        cells_list[cell_center.index_list + 2 - (change_line * 4)],
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list + 2 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list - 2 + change_line],
        cells_list[cell_center.index_list - 4 + change_line],
        cells_list[cell_center.index_list - 4 + (change_line * 2)],
        cells_list[cell_center.index_list + 4 + change_line],
        cells_list[cell_center.index_list + 4 + (change_line * 2)],
        cells_list[cell_center.index_list - 1 + (change_line * 2)],
        cells_list[cell_center.index_list + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 2)],
    ]

    symbole_invaders_add: list[Cells] = [
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list - 1 - change_line],
    ]
    list_symbole.append(symbole_invaders)
    list_symbole.append(symbole_invaders_add)

    match symbole_index:
        case 0:
            for case in symbole_42:
                change_state(case, lab_str, True, False)
            change_wall_cell(cells_list, symbole_42, size_values)
        case 1:
            for case in symbole_invaders:
                change_state(case, lab_str, True, False)
            for case in symbole_invaders_add:
                change_state(case, lab_str, False, True)
            change_wall_cell(cells_list, symbole_invaders, size_values)

    return symbole_42


def change_wall_cell(
    cells_list: list[Cells], symbol_lst: list[Cells], size_values: list[int]
) -> None:
    change_line: int = (size_values[0] * 2) - 1

    for c in symbol_lst:
        cells_list[c.index_list - 1].walls["E"] = False
        cells_list[c.index_list + 1].walls["W"] = False
        cells_list[c.index_list - change_line].walls["S"] = False
        cells_list[c.index_list + change_line].walls["N"] = False
        cells_list[c.index_list - 2].walls["E"] = False
        cells_list[c.index_list + 2].walls["W"] = False
        cells_list[c.index_list - change_line * 2].walls["S"] = False
        cells_list[c.index_list + change_line * 2].walls["N"] = False


def symbol_logic(
    cells_list: list[Cells],
    size_values: list[int],
    lab_str: list[str],
    symbole_index: int,
) -> list[Cells]:
    center: tuple[int, int] = find_center(size_values)

    return center_symbol(cells_list, center, size_values, lab_str, symbole_index)
