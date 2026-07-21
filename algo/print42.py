from classes import Cells
from .wall_destroyer import change_state


def find_center(size_values: list[int]) -> tuple[int, int]:
    x_range: int = size_values[0] * 2
    x_center: int = int((x_range - 2) / 2)

    y_range: int = size_values[1] * 2
    y_center: int = int((y_range - 2) / 2)

    return (x_center, y_center)


def center_symbol(
    cells_list: list[Cells],
    center: tuple[int, int],
    size_values: list[int],
    lab_str: list[str],
) -> None:
    cell_center: Cells = cells_list[0]
    change_line: int = (size_values[0] * 2) - 1

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

    for case in symbole_42:
        change_state(case, lab_str, True)


def symbol_logic(
    cells_list: list[Cells], size_values: list[int], lab_str: list[str]
) -> None:
    center: tuple[int, int] = find_center(size_values)
    center_symbol(cells_list, center, size_values, lab_str)
