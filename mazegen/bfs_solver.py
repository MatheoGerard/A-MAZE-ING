from .cells_class import Cells


def find_start(cell_list: list[Cells]) -> Cells:
    """
    Find the starting cell of the maze.

    The function searches through the list of cells and returns the first cell
    marked as the entry point. If no entry cell is found, it returns the first
    cell in the list as a fallback.

    Args:
        cell_list: List of all cells composing the maze.

    Returns:
        The cell representing the maze starting point.
    """
    default_return: Cells = cell_list[0]
    for c in cell_list:
        if c.is_entry:
            return c
    return default_return


def find_finish(cell_list: list[Cells]) -> Cells:
    """
    Find the finishing cell of the maze.

    The function searches through the list of cells and returns the first cell
    marked as the exit point. If no exit cell is found, it returns the first
    cell in the list as a fallback.

    Args:
        cell_list: List of all cells composing the maze.

    Returns:
        The cell representing the maze finishing point.
    """
    default_return: Cells = cell_list[0]
    for c in cell_list:
        if c.is_exit:
            return c
    return default_return


def finish_check(finish_cell: Cells) -> bool:
    """
    Check whether the finish cell has been reached.

    The function determines if the exit cell has already been used, which
    indicates that the player has reached the end of the maze.

    Args:
        finish_cell: The maze cell representing the exit.

    Returns:
        ``True`` if the finish cell has been reached, otherwise ``False``.
    """
    if finish_cell.is_used:
        return True

    return False


def find_possibilities(
    cell_list: list[Cells], current: Cells, size_values: list[int]
) -> list[str]:
    """
    Find all possible movements from the current cell.

    The function checks the neighboring cells of the current position and
    returns the directions where movement is possible. A direction is valid
    when the adjacent cell is inside the maze boundaries and is walkable.

    Args:
        cell_list: List of all cells composing the maze.
        current: The current cell from which possible moves are checked.
        size_values: Dimensions of the maze.

    Returns:
        A list of available directions represented by their cardinal letters
        (``N``, ``S``, ``E``, ``W``).
    """
    list_direction: list[str] = []
    change_line: int = (size_values[0] * 2) - 1

    if current.position[1] != (size_values[1] * 2) - 2 and (
        cell_list[current.index_list + change_line].char == " "
        or cell_list[current.index_list + change_line].char == "E"
        or cell_list[current.index_list + change_line].char == "e"
    ):
        list_direction.append("S")
    if current.position[1] != 0 and (
        cell_list[current.index_list - change_line].char == " "
        or cell_list[current.index_list - change_line].char == "E"
        or cell_list[current.index_list - change_line].char == "e"
    ):
        list_direction.append("N")
    if current.position[0] != 0 and (
        cell_list[current.index_list - 1].char == " "
        or cell_list[current.index_list - 1].char == "E"
        or cell_list[current.index_list - 1].char == "e"
    ):
        list_direction.append("W")
    if current.position[0] != (size_values[0] * 2) - 2 and (
        cell_list[current.index_list + 1].char == " "
        or cell_list[current.index_list + 1].char == "E"
        or cell_list[current.index_list + 1].char == "e"
    ):
        list_direction.append("E")

    return list_direction


def bfs_function(
    cell_list: list[Cells], size_values: list[int]
) -> list[Cells | str]:
    """
    Find the shortest path from the maze entry to the exit using BFS.

    The function applies a Breadth-First Search algorithm to explore the maze
    from the starting cell. It keeps track of visited cells, explores possible
    directions, and returns the first path that reaches the exit.

    Args:
        cell_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.

    Returns:
        A list containing the cells and directions composing the shortest path
        to the exit. Returns an empty list if no path is found.
    """
    start: Cells = find_start(cell_list)
    change_line: int = (size_values[0] * 2) - 1
    is_exit_find: bool = False

    current: Cells = start
    all_ways: list[list[Cells | str]] = []

    first_way: list[Cells | str] = []
    first_way.append(current)

    all_ways.append(first_way)
    current.is_solved = True

    default_return: list[Cells | str] = []

    while not is_exit_find:
        new_list: list[Cells | str] = []
        possibilities: list[str] = []

        for ways in all_ways:
            if isinstance(ways[0], Cells):
                possibilities = find_possibilities(
                    cell_list, ways[0], size_values
                )

            for x in possibilities:
                if x == "N":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[
                            ways[0].index_list - change_line
                        ]
                        if isinstance(new_list[0], Cells):
                            if not new_list[0].is_solved:
                                new_list[0].is_solved = True
                                new_list.append("N")
                                all_ways.append(new_list)
                                if new_list[0].is_exit:
                                    is_exit_find = True
                                    return new_list
                if x == "S":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[
                            ways[0].index_list + change_line
                        ]
                        if isinstance(new_list[0], Cells):
                            if not new_list[0].is_solved:
                                new_list[0].is_solved = True
                                new_list.append("S")
                                all_ways.append(new_list)
                                if new_list[0].is_exit:
                                    is_exit_find = True
                                    return new_list
                if x == "E":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list + 1]
                        if isinstance(new_list[0], Cells):
                            if not new_list[0].is_solved:
                                new_list[0].is_solved = True
                                new_list.append("E")
                                all_ways.append(new_list)
                                if new_list[0].is_exit:
                                    is_exit_find = True
                                    return new_list
                if x == "W":
                    new_list = ways.copy()
                    if isinstance(ways[0], Cells):
                        new_list[0] = cell_list[ways[0].index_list - 1]
                        if isinstance(new_list[0], Cells):
                            if not new_list[0].is_solved:
                                new_list[0].is_solved = True
                                new_list.append("W")
                                all_ways.append(new_list)
                                if new_list[0].is_exit:
                                    is_exit_find = True
                                    return new_list
    return default_return
