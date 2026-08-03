import readchar
from mazegen import Cells


def input_read() -> str:
    """
    Read a single key press from the keyboard.

    The function waits for the user to press a key and returns it without
    requiring the Enter key.

    Returns:
        The character corresponding to the pressed key.
    """
    return readchar.readkey()


def go_north(
    current: Cells,
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
) -> Cells:
    """
    Move the player one cell to the north if the path is accessible.

    The function checks that the player is not at the top boundary and that
    the destination cell is walkable. If the move is valid, it updates the
    maze representation and returns the player's new position.

    Args:
        current: The player's current cell.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        The player's current cell after attempting the move.
    """
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
    """
    Move the player one cell to the go_south if the path is accessible.

    The function checks that the player is not at the bottom boundary and that
    the destination cell is walkable. If the move is valid, it updates the
    maze representation and returns the player's new position.

    Args:
        current: The player's current cell.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        The player's current cell after attempting the move.
    """

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
    """
    Move the player one cell to the east if the path is accessible.

    The function checks that the player is not at the right boundary and that
    the destination cell is walkable. If the move is valid, it updates the
    maze representation and returns the player's new position.

    Args:
        current: The player's current cell.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        The player's current cell after attempting the move.
    """
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
    """
    Move the player one cell to the west if the path is accessible.

    The function checks that the player is not at the left boundary and that
    the destination cell is walkable. If the move is valid, it updates the
    maze representation and returns the player's new position.

    Args:
        current: The player's current cell.
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.

    Returns:
        The player's current cell after attempting the move.
    """
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
