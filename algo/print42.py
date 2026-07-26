from classes import Cells
from .wall_destroyer import change_state


def find_center(cells_list: list[Cells], size_values: list[int]) -> Cells:
    default_return: Cells = cells_list[0]

    x_range: int = size_values[0] * 2
    x_center: int = int((x_range - 2) / 2)

    y_range: int = size_values[1] * 2
    y_center: int = int((y_range - 2) / 2)

    for c in cells_list:
        if c.position[0] == x_center and c.position[1] == y_center:
            return c

    return default_return


def change_symbole(index: int, symbole_nb: int) -> int:
    if index == symbole_nb - 1:
        return 0
    else:
        return index + 1


def center_symbol(
    cells_list: list[Cells],
    size_values: list[int],
    lab_str: list[str],
    symbole_index: int,
) -> list[Cells]:
    cell_center: Cells = find_center(cells_list, size_values)
    change_line: int = (size_values[0] * 2) - 1
    list_symbole: list[list[Cells]] = []

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

    symbole_heart: list[Cells] = [
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
        cells_list[cell_center.index_list - (change_line * 2)],
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + (change_line * 2)],
        cells_list[cell_center.index_list + (change_line * 3)],
        cells_list[cell_center.index_list + (change_line * 4)],
        cells_list[cell_center.index_list - 1 - change_line],
        cells_list[cell_center.index_list - 2 - change_line],
        cells_list[cell_center.index_list - 3 - change_line],
        cells_list[cell_center.index_list - 4 - change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list + 2 - change_line],
        cells_list[cell_center.index_list + 3 - change_line],
        cells_list[cell_center.index_list + 4 - change_line],
        cells_list[cell_center.index_list - 1 - (change_line * 2)],
        cells_list[cell_center.index_list - 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 3 - (change_line * 2)],
        cells_list[cell_center.index_list - 4 - (change_line * 2)],
        cells_list[cell_center.index_list + 1 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 - (change_line * 2)],
        cells_list[cell_center.index_list + 3 - (change_line * 2)],
        cells_list[cell_center.index_list + 4 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 3)],
        cells_list[cell_center.index_list - 2 - (change_line * 3)],
        cells_list[cell_center.index_list - 3 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 - (change_line * 3)],
        cells_list[cell_center.index_list + 2 - (change_line * 3)],
        cells_list[cell_center.index_list + 3 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list + 2 + change_line],
        cells_list[cell_center.index_list + 3 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list - 2 + change_line],
        cells_list[cell_center.index_list - 3 + change_line],
        cells_list[cell_center.index_list - 1 + (change_line * 2)],
        cells_list[cell_center.index_list - 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 2)],
        cells_list[cell_center.index_list + 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 3)],
        cells_list[cell_center.index_list - 1 + (change_line * 3)],
    ]

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
        case 2:
            for case in symbole_heart:
                change_state(case, lab_str, True, False)
            change_wall_cell(cells_list, symbole_heart, size_values)

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
    return center_symbol(cells_list, size_values, lab_str, symbole_index)
