import time
from classes import Cells
import visualization as visu
from rich.console import Console
from rich.live import Live
from rich.text import Text


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


def find_possibilities(
    cell_list: list[Cells], current: Cells, size_values: list[int]
) -> list[str]:
    list_direction: list[str] = []
    change_line: int = (size_values[0] * 2) - 1

    if current.position[1] != (size_values[1] * 2) - 2 and (
        cell_list[current.index_list + change_line].char == " "
        or cell_list[current.index_list + change_line].char == "E"
    ):
        list_direction.append("S")
    if current.position[1] != 0 and (
        cell_list[current.index_list - change_line].char == " "
        or cell_list[current.index_list - change_line].char == "E"
    ):
        list_direction.append("N")
    if current.position[0] != 0 and (
        cell_list[current.index_list - 1].char == " "
        or cell_list[current.index_list - 1].char == "E"
    ):
        list_direction.append("W")
    if current.position[0] != (size_values[0] * 2) - 2 and (
        cell_list[current.index_list + 1].char == " "
        or cell_list[current.index_list + 1].char == "E"
    ):
        list_direction.append("E")

    return list_direction


def bfs_function(cell_list: list[Cells], size_values: list[int]) -> list[Cells | str]:
    start: Cells | None = find_start(cell_list)
    finish: Cells | None = find_finish(cell_list)
    change_line: int = (size_values[0] * 2) - 1
    is_exit_find: bool = False

    if not finish:
        raise ValueError("No finish found")
    if not start:
        raise ValueError("No start found")

    current: Cells = start
    all_ways: list[list[Cells | str]] = []

    first_way: list[Cells | str] = []
    first_way.append(current)

    all_ways.append(first_way)
    current.is_solved = True

    while not is_exit_find:
        new_list: list[Cells | str] = []
        possibilities: list[str] = []

        for ways in all_ways:
            if isinstance(ways[0], Cells):
                possibilities: list[str] = find_possibilities(
                    cell_list, ways[0], size_values
                )

            for x in possibilities:
                if x == "N":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list - change_line]
                        if not new_list[0].is_solved:
                            new_list[0].is_solved = True
                            new_list.append("N")
                            all_ways.append(new_list)
                    if isinstance(new_list[0], Cells):
                        if new_list[0].is_exit:
                            is_exit_find = True
                            return new_list
                if x == "S":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list + change_line]
                        if not new_list[0].is_solved:
                            new_list[0].is_solved = True
                            new_list.append("S")
                            all_ways.append(new_list)
                    if isinstance(new_list[0], Cells):
                        if new_list[0].is_exit:
                            is_exit_find = True
                            return new_list
                if x == "E":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list + 1]
                        if not new_list[0].is_solved:
                            new_list[0].is_solved = True
                            new_list.append("E")
                            all_ways.append(new_list)
                    if isinstance(new_list[0], Cells):
                        if new_list[0].is_exit:
                            is_exit_find = True
                            return new_list
                if x == "W":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list - 1]
                        if not new_list[0].is_solved:
                            new_list[0].is_solved = True
                            new_list.append("W")
                            all_ways.append(new_list)
                    if isinstance(new_list[0], Cells):
                        if new_list[0].is_exit:
                            is_exit_find = True
                            return new_list


def solver_print(
    entry: Cells,
    soluce: list[Cells | str],
    lab_lst: list[str],
    cell_list: list[Cells],
    size_values: list[int],
    color_set: str,
    console: Console,
    is_anim: bool,
) -> list[str]:
    change_line: int = (size_values[0] * 2) - 1
    current: Cells = entry

    for w in soluce[1:]:
        match w:
            case "N":
                cell_list[current.index_list - change_line].char = "S"
                lab_lst[current.index_str - change_line - 3] = "S"
                current = cell_list[current.index_list - change_line]
            case "S":
                cell_list[current.index_list + change_line].char = "S"
                lab_lst[current.index_str + change_line + 3] = "S"
                current = cell_list[current.index_list + change_line]
            case "E":
                cell_list[current.index_list + 1].char = "S"
                lab_lst[current.index_str + 1] = "S"
                current = cell_list[current.index_list + 1]
            case "W":
                cell_list[current.index_list - 1].char = "S"
                lab_lst[current.index_str - 1] = "S"
                current = cell_list[current.index_list - 1]
        if is_anim:
            print("\033[H", end="")
            visu.visualizatoin_format(lab_lst, color_set, console)
            time.sleep(0.00000000005)

    return lab_lst
