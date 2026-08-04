from .cells_class import Cells


def change_state(
    cell: Cells, lab_lst: list[str], is_symbole: bool, is_symbole_add: bool
) -> None:
    if is_symbole:
        lab_lst[cell.index_str] = "L"
        cell.char = "L"
    elif is_symbole_add:
        lab_lst[cell.index_str] = "Y"
        cell.char = "Y"
    elif cell.char == "#":
        lab_lst[cell.index_str] = " "
        cell.char = " "
