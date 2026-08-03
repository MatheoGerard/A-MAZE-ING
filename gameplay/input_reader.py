import readchar
from mazegen import Cells


def input_read() -> str:
    return readchar.readkey()


def go_north(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> Cells:
    change_line: int = (size_values[0] * 2) - 1

    if current.position[1] != 0:
        if (
            cells_list[current.index_list - change_line].char == " "
            or cells_list[current.index_list - change_line].char == "E"
            or cells_list[current.index_list - change_line].char == "e"
            or cells_list[current.index_list - change_line].char == "S"
        ):
            current.char = " "
            lab_lst[current.index_str] = " "
            cells_list[current.index_list - change_line].char = "P"
            lab_lst[current.index_str - 3 - change_line] = "P"
            current = cells_list[current.index_list - change_line]

    return current


def go_south(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> Cells:
    change_line: int = (size_values[0] * 2) - 1

    if current.position[1] != (size_values[1] * 2) - 2:
        if (
            cells_list[current.index_list + change_line].char == " "
            or cells_list[current.index_list + change_line].char == "e"
            or cells_list[current.index_list + change_line].char == "E"
            or cells_list[current.index_list + change_line].char == "S"
        ):
            current.char = " "
            lab_lst[current.index_str] = " "
            cells_list[current.index_list + change_line].char = "P"
            lab_lst[current.index_str + 3 + change_line] = "P"
            current = cells_list[current.index_list + change_line]

    return current


def go_east(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> Cells:
    if current.position[0] != (size_values[0] * 2) - 2:
        if (
            cells_list[current.index_list + 1].char == " "
            or cells_list[current.index_list + 1].char == "E"
            or cells_list[current.index_list + 1].char == "e"
            or cells_list[current.index_list + 1].char == "S"
        ):
            current.char = " "
            lab_lst[current.index_str] = " "
            cells_list[current.index_list + 1].char = "P"
            lab_lst[current.index_str + 1] = "P"
            current = cells_list[current.index_list + 1]

    return current


def go_west(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> Cells:
    if current.position[0] != 0:
        if (
            cells_list[current.index_list - 1].char == " "
            or cells_list[current.index_list - 1].char == "e"
            or cells_list[current.index_list - 1].char == "E"
            or cells_list[current.index_list - 1].char == "S"
        ):
            current.char = " "
            lab_lst[current.index_str] = " "
            cells_list[current.index_list - 1].char = "P"
            lab_lst[current.index_str - 1] = "P"
            current = cells_list[current.index_list - 1]

    return current
