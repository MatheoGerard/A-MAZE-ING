from classes import Cells


def change_line(current: Cells, size_value: list[int]) -> int:
    return (size_value[0] * 2) - 2


def go_up(
    current: Cells, cells_list: list[Cells], size_value: list[int], history: list[Cells]
) -> bool:
    change_line: int = (size_value[0] * 2) - 2

    if cells_list[current.index_list - change_line].char == " ":
        history.append(cells_list[current.index_list - change_line])
        history.append(cells_list[current.index_list - (change_line * 2)])
        return True

    return False


def go_down(
    current: Cells, cells_list: list[Cells], size_value: list[int], history: list[Cells]
) -> bool:
    change_line: int = (size_value[0] * 2) - 2

    if cells_list[current.index_list + change_line].char == " ":
        history.append(cells_list[current.index_list + change_line])
        history.append(cells_list[current.index_list + (change_line * 2)])
        return True

    return False


def go_east(current: Cells, cells_list: list[Cells], history: list[Cells]) -> bool:
    if cells_list[current.index_list + 1].char == " ":
        history.append(cells_list[current.index_list + 1])
        history.append(cells_list[current.index_list + 2])
        return True

    return False


def go_west(current: Cells, cells_list: list[Cells], history: list[Cells]) -> bool:
    if cells_list[current.index_list - 1].char == " ":
        history.append(cells_list[current.index_list - 1])
        history.append(cells_list[current.index_list - 2])
        return True

    return False
