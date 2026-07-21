from classes import Cells


def change_state(cell: Cells, lab_lst: list[str], is_symbole: bool) -> None:
    if is_symbole:
        lab_lst[cell.index_str] = "L"
        cell.char = "L"
    elif cell.char == "#":
        lab_lst[cell.index_str] = " "
        cell.char = " "


def generator(cells: list[Cells]) -> None:
    pass
