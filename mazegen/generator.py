from .cells_class import Cells
import random


def back_track(
    cells_list: list[Cells],
    cell: Cells,
    direction_history: list[str],
    size_values: list[int],
) -> Cells:
    """
    Move backwards through the generated path to find a cell with available
    directions.

    The function performs a backtracking operation by following the reverse of
    the previously taken directions until it reaches a cell where a new path
    can be explored or until there are no more directions to undo.

    Args:
        cells_list: List of all cells composing the maze.
        cell: Current cell from which the backtracking starts.
        direction_history: List containing the history of visited directions.
        size_values: Dimensions of the maze.

    Returns:
        The last cell reached during backtracking where a new direction can be
        chosen.
    """
    change_line: int = (size_values[0] * 2) - 1
    current_cell: Cells = cell
    last_dir: str = ""

    while not choice_direction(cells_list, current_cell, size_values):
        if len(direction_history) == 0:
            break

        last_dir = direction_history.pop()

        if last_dir == "N":
            current_cell = cells_list[
                current_cell.index_list + change_line * 2
            ]
        elif last_dir == "S":
            current_cell = cells_list[
                current_cell.index_list - change_line * 2
            ]
        elif last_dir == "E":
            current_cell = cells_list[current_cell.index_list - 2]
        elif last_dir == "W":
            current_cell = cells_list[current_cell.index_list + 2]

    return current_cell


def choice_direction(
    cells_list: list[Cells],
    cell: Cells,
    size_values: list[int],
) -> str:
    """
    Choose a random available direction from the current cell.

    The function checks the possible neighboring cells, removes invalid or
    already visited directions, and randomly selects one of the remaining
    directions.

    Args:
        cells_list: List of all cells composing the maze.
        cell: Current cell from which a direction is chosen.
        size_values: Dimensions of the maze.

    Returns:
        A randomly selected direction (``N``, ``S``, ``E``, or ``W``).
        Returns an empty string if no direction is available.
    """
    dir: str = ""
    dir_list: list[str] = []

    change_line: int = (size_values[0] * 2) - 1

    dir_list = ["N", "E", "S", "W"]

    if not cell.walls["N"]:
        dir_list.remove("N")
    if not cell.walls["S"]:
        dir_list.remove("S")
    if not cell.walls["E"]:
        dir_list.remove("E")
    if not cell.walls["W"]:
        dir_list.remove("W")

    if "N" in dir_list:
        if cells_list[cell.index_list - change_line * 2].is_used:
            dir_list.remove("N")

    if "S" in dir_list:
        if cells_list[cell.index_list + change_line * 2].is_used:
            dir_list.remove("S")

    if "E" in dir_list:
        if cells_list[cell.index_list + 2].is_used:
            dir_list.remove("E")

    if "W" in dir_list:
        if cells_list[cell.index_list - 2].is_used:
            dir_list.remove("W")

    if len(dir_list) == 0:
        return ""
    else:
        dir = random.choice(dir_list)

    return dir


def change_cell_state(
    cell: Cells,
    dir: str,
    size_values: list[int],
    cells_list: list[Cells],
    lab_lst: list[str],
) -> None:
    """
    Update the state of a neighboring cell during maze generation.

    The function removes the wall between the current cell and the selected
    neighboring direction by updating the cell character and the maze string
    representation.

    Args:
        cell: Current cell from which the wall is removed.
        dir: Direction of the neighboring cell to open.
        size_values: Dimensions of the maze.
        cells_list: List of all cells composing the maze.
        lab_lst: List representing the current maze state.

    Returns:
        None
    """
    change_line: int = (size_values[0] * 2) - 1

    if dir == "N":
        cells_list[cell.index_list - (change_line)].char = " "
        lab_lst[cell.index_str - change_line - 3] = " "
    elif dir == "E":
        cells_list[cell.index_list + 1].char = " "
        lab_lst[cell.index_str + 1] = " "
    elif dir == "S":
        cells_list[cell.index_list + (change_line)].char = " "
        lab_lst[cell.index_str + change_line + 3] = " "
    elif dir == "W":
        cells_list[cell.index_list - 1].char = " "
        lab_lst[cell.index_str - 1] = " "


def finish_check(cell_list: list[Cells]) -> bool:
    """
    Check whether the maze generation is complete.

    The function verifies that all valid maze cells have been visited during
    generation. A maze is considered finished when every non-wall cell with
    valid coordinates has been marked as used.

    Args:
        cell_list: List of all cells composing the maze.

    Returns:
        ``True`` if all maze cells have been visited, otherwise ``False``.
    """
    for c in cell_list:
        if c.position[0] % 2 == 0 and c.position[1] % 2 == 0:
            if not c.is_used:
                return False

    return True


def change_current_cell(
    cell: Cells, cells_list: list[Cells], size_values: list[int], dir: str
) -> Cells:
    """
    Get the neighboring cell in the specified direction.

    The function calculates and returns the cell located in the given
    direction from the current cell based on the maze dimensions.

    Args:
        cell: Current cell from which the movement starts.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        dir: Direction of movement (``N``, ``E``, ``S``, or ``W``).

    Returns:
        The cell located in the selected direction.
    """
    change_line: int = (size_values[0] * 2) - 1

    if dir == "N":
        return cells_list[cell.index_list - (change_line * 2)]
    elif dir == "E":
        return cells_list[cell.index_list + 2]
    elif dir == "S":
        return cells_list[cell.index_list + (change_line * 2)]
    else:
        return cells_list[cell.index_list - 2]


def check_north(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> bool:
    """
    Check whether movement to the north is possible.

    The function verifies that there is no wall blocking the north direction
    and that the neighboring cell is a valid walkable cell.

    Args:
        current: Current cell from which the movement is checked.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.

    Returns:
        ``True`` if the north direction is available, otherwise ``False``.
    """
    if not current.walls["N"]:
        return False

    change_line: int = (size_values[0] * 2) - 1

    if (
        cells_list[current.index_list - (change_line * 2)].char == " "
        or cells_list[current.index_list - (change_line * 2)].char == "E"
        or cells_list[current.index_list - (change_line * 2)].char == "e"
    ):
        return True

    return False


def check_south(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> bool:
    """
    Check whether movement to the south is possible.

    The function verifies that there is no wall blocking the south direction
    and that the neighboring cell is a valid walkable cell.

    Args:
        current: Current cell from which the movement is checked.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.

    Returns:
        ``True`` if the south direction is available, otherwise ``False``.
    """
    if not current.walls["S"]:
        return False

    change_line: int = (size_values[0] * 2) - 1

    if (
        cells_list[current.index_list + (change_line * 2)].char == " "
        or cells_list[current.index_list + (change_line * 2)].char == "E"
        or cells_list[current.index_list + (change_line * 2)].char == "e"
    ):
        return True

    return False


def check_east(current: Cells, cells_list: list[Cells]) -> bool:
    """
    Check whether movement to the east is possible.

    The function verifies that there is no wall blocking the east direction
    and that the neighboring cell is a valid walkable cell.

    Args:
        current: Current cell from which the movement is checked.
        cells_list: List of all cells composing the maze.

    Returns:
        ``True`` if the east direction is available, otherwise ``False``.
    """
    if not current.walls["E"]:
        return False

    if (
        cells_list[current.index_list + 2].char == " "
        or cells_list[current.index_list + 2].char == "E"
        or cells_list[current.index_list + 2].char == "e"
    ):
        return True

    return False


def check_west(current: Cells, cells_list: list[Cells]) -> bool:
    """
    Check whether movement to the west is possible.

    The function verifies that there is no wall blocking the west direction
    and that the neighboring cell is a valid walkable cell.

    Args:
        current: Current cell from which the movement is checked.
        cells_list: List of all cells composing the maze.

    Returns:
        ``True`` if the west direction is available, otherwise ``False``.
    """
    if not current.walls["W"]:
        return False

    if (
        cells_list[current.index_list - 2].char == " "
        or cells_list[current.index_list - 2].char == "E"
        or cells_list[current.index_list - 2].char == "e"
    ):
        return True

    return False


def check_dead_ends(
    current: Cells, cells_list: list[Cells], size_values: list[int]
) -> tuple[bool, str | None]:
    """
    Check whether the current cell is a dead end.

    The function checks all available neighboring cells and determines if the
    current cell has only one possible direction to continue. A dead end is
    identified when exactly one valid direction is available.

    Args:
        current: Current cell to check.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.

    Returns:
        A tuple containing:
            - A boolean indicating whether the cell is a dead end.
            - The only available direction if it is a dead end, otherwise
              ``None``.
    """
    nb_direction: list[str] = []
    change_line: int = (size_values[0] * 2) - 1

    if current.position[0] != (size_values[0] * 2) - 2 and (
        cells_list[current.index_list + 1].char == " "
        or cells_list[current.index_list + 1].char == "E"
        or cells_list[current.index_list + 1].char == "e"
    ):
        nb_direction.append("E")

    if current.position[0] != 0 and (
        cells_list[current.index_list - 1].char == " "
        or cells_list[current.index_list - 1].char == "E"
        or cells_list[current.index_list - 1].char == "e"
    ):
        nb_direction.append("W")

    if current.position[1] != (size_values[1] * 2) - 2 and (
        cells_list[current.index_list + change_line].char == " "
        or cells_list[current.index_list + change_line].char == "E"
        or cells_list[current.index_list + change_line].char == "e"
    ):
        nb_direction.append("S")

    if current.position[1] != 0 and (
        cells_list[current.index_list - change_line].char == " "
        or cells_list[current.index_list - change_line].char == "E"
        or cells_list[current.index_list - change_line].char == "e"
    ):
        nb_direction.append("N")

    if len(nb_direction) == 1:
        return (True, nb_direction[0])

    return (False, None)


def destroy_dead_ends(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> None:
    """
    Remove dead ends by opening an additional path.

    The function detects if the current cell is a dead end and, when possible,
    randomly opens a connection to another available direction to reduce maze
    dead ends.

    Args:
        current: Current cell from which dead-end removal is attempted.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        None
    """
    list_direction: list[str] = []
    check: tuple[bool, str | None] = check_dead_ends(
        current, cells_list, size_values
    )
    change_line: int = (size_values[0] * 2) - 1

    if check[0]:
        if check_north(current, cells_list, size_values):
            list_direction.append("N")
        if check_south(current, cells_list, size_values):
            list_direction.append("S")
        if check_east(current, cells_list):
            list_direction.append("E")
        if check_west(current, cells_list):
            list_direction.append("W")

    if check[1]:
        if len(list_direction) > 1:
            list_direction.remove(check[1])

    if len(list_direction) > 0:
        direction_to_go: str = random.choice(list_direction)

        if direction_to_go == "N":
            cells_list[current.index_list - change_line].char = " "
            lab_lst[current.index_str - change_line - 3] = " "
        if direction_to_go == "S":
            cells_list[current.index_list + change_line].char = " "
            lab_lst[current.index_str + change_line + 3] = " "
        if direction_to_go == "W":
            cells_list[current.index_list - 1].char = " "
            lab_lst[current.index_str - 1] = " "
        if direction_to_go == "E":
            cells_list[current.index_list + 1].char = " "
            lab_lst[current.index_str + 1] = " "


def unperfect(
    cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> None:
    """
    Convert a perfect maze into an imperfect maze.

    The function removes some dead ends by opening additional paths between
    cells, then modifies the center area of the maze to create more complex
    passages.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        None
    """
    for c in cells_list:
        if c.char == " " or c.char == "E" or c.char == "e":
            destroy_dead_ends(c, cells_list, size_values, lab_lst)


def gen_maze(
    cells_list: list[Cells], size_values: list[int], lab_lst: list[str]
) -> list[str]:
    """
    Generate the maze using a backtracking algorithm.

    The function creates a maze by exploring available directions from each
    cell, opening passages between cells, and using backtracking when no
    further movement is possible. The process continues until all maze cells
    have been visited.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        The updated maze representation containing the generated paths.
    """
    current: Cells = cells_list[0]
    direction_history: list[str] = []
    current.is_used = True

    while not finish_check(cells_list):
        direction: str = choice_direction(cells_list, current, size_values)
        if not direction:
            current = back_track(
                cells_list, current, direction_history, size_values
            )
            if len(direction_history) == 0:
                break
            continue
        direction_history.append(direction)
        change_cell_state(current, direction, size_values, cells_list, lab_lst)
        current = change_current_cell(
            current, cells_list, size_values, direction
        )
        current.is_used = True
    return lab_lst
