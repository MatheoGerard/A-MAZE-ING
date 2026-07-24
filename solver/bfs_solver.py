from classes import Cells
from .direction_functions import go_up, go_down, go_east, go_west


def find_start(cell_list: list[Cells]) -> Cells | None:
    for c in cell_list:
        if c.is_entry:
            return c


def find_finish(cell_list: list[Cells]) -> Cells | None:
    for c in cell_list:
        if c.is_exit:
            return c


def finish_check(finish_cell: Cells) -> bool:
    if finish_cell.is_used:
        return True

    return False


def bfs_function(cell_list: list[Cells], entry_exit: list[list[int]]) -> None:
    start: Cells | None = find_start(cell_list)
    finish: Cells | None = find_finish(cell_list)

    if not finish:
        raise ValueError("No finish found")
    if not start:
        raise ValueError("No start found")

    current: Cells = start
    all_ways: list[list[Cells]] = []

    while not finish_check(finish):


