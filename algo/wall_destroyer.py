from classes import Cells


def change_state(cell: Cells, lab_lst: list[str]) -> None:
    if cell.char == "#":
        lab_lst[cell.index_str] = " "
        cell.char = " "
