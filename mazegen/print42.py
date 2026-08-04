from .cells_class import Cells
from .wall_destroyer import change_state


def find_center(cells_list: list[Cells], size_values: list[int]) -> Cells:
    """
    Find the center cell of the maze.

    The function calculates the center coordinates according to the maze
    dimensions and returns the corresponding cell. It handles both even and
    odd maze sizes to locate the correct central position.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.

    Returns:
        The cell located at the center of the maze.
    """
    default_return: Cells = cells_list[0]

    x_range: int = size_values[0] * 2
    x_center: int = int((x_range - 2) / 2)

    y_range: int = size_values[1] * 2
    y_center: int = int((y_range - 2) / 2)

    for c in cells_list:
        if size_values[0] % 2 == 0 and size_values[1] % 2 == 0:
            if c.position[0] + 1 == x_center and c.position[1] + 1 == y_center:
                return c
        elif size_values[0] % 2 == 0 and size_values[1] % 2 != 0:
            if c.position[0] + 1 == x_center and c.position[1] == y_center:
                return c
        elif size_values[0] % 2 != 0 and size_values[1] % 2 == 0:
            if c.position[0] == x_center and c.position[1] + 1 == y_center:
                return c
        else:
            if c.position[0] == x_center and c.position[1] == y_center:
                return c

    return default_return


def change_symbole(index: int, symbole_nb: int) -> int:
    """
    Change the current symbol index.

    The function increments the symbol index and resets it to zero when the
    last available symbol is reached.

    Args:
        index: Current symbol index.
        symbole_nb: Number of available symbols.

    Returns:
        The updated symbol index.
    """
    if index == symbole_nb - 1:
        return 0
    else:
        return index + 1


def center_symbol(
    cells_list: list[Cells],
    size_values: list[int],
    lab_str: list[str],
    symbole_index: int,
) -> list[Cells]:
    """
    Draw a symbol in the center of the maze.

    The function selects a predefined symbol pattern, modifies the maze cells
    around the center, and updates the maze representation by opening the
    required passages.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_str: List representing the current maze state.
        symbole_index: Index of the symbol to draw.

    Returns:
        A list of cells used by the selected symbol.
    """
    cell_center: Cells = find_center(cells_list, size_values)
    change_line: int = (size_values[0] * 2) - 1
    list_symbole: list[list[Cells]] = []

    symbole_42: list[Cells] = [
        cells_list[cell_center.index_list - 2],
        cells_list[cell_center.index_list - 4],
        cells_list[cell_center.index_list - 6],
        cells_list[cell_center.index_list - 6 - (change_line * 2)],
        cells_list[cell_center.index_list - 6 - (change_line * 4)],
        cells_list[cell_center.index_list - 2 + (change_line * 2)],
        cells_list[cell_center.index_list - 2 + (change_line * 4)],
        cells_list[cell_center.index_list + 2],
        cells_list[cell_center.index_list + 4],
        cells_list[cell_center.index_list + 6],
        cells_list[cell_center.index_list + 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 2 + (change_line * 4)],
        cells_list[cell_center.index_list + 6 - (change_line * 2)],
        cells_list[cell_center.index_list + 6 - (change_line * 4)],
        cells_list[cell_center.index_list + 4 - (change_line * 4)],
        cells_list[cell_center.index_list + 2 - (change_line * 4)],
        cells_list[cell_center.index_list + 4 + (change_line * 4)],
        cells_list[cell_center.index_list + 6 + (change_line * 4)],
    ]
    list_symbole.append(symbole_42)

    symbole_invaders: list[Cells] = [
        cells_list[cell_center.index_list],
        cells_list[cell_center.index_list - 1],
        cells_list[cell_center.index_list - 2],
        cells_list[cell_center.index_list - 3],
        cells_list[cell_center.index_list - 4],
        cells_list[cell_center.index_list + 1],
        cells_list[cell_center.index_list + 2],
        cells_list[cell_center.index_list + 3],
        cells_list[cell_center.index_list + 4],
        cells_list[cell_center.index_list - change_line],
        cells_list[cell_center.index_list - 1 - change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list - 2 - change_line],
        cells_list[cell_center.index_list + 2 - change_line],
        cells_list[cell_center.index_list - 3 - change_line],
        cells_list[cell_center.index_list + 3 - change_line],
        cells_list[cell_center.index_list - (change_line * 2)],
        cells_list[cell_center.index_list + 1 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 2)],
        cells_list[cell_center.index_list - 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 - (change_line * 3)],
        cells_list[cell_center.index_list - 1 - (change_line * 4)],
        cells_list[cell_center.index_list + 1 - (change_line * 4)],
        cells_list[cell_center.index_list - 2 - (change_line * 4)],
        cells_list[cell_center.index_list + 2 - (change_line * 4)],
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list + 2 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list - 2 + change_line],
        cells_list[cell_center.index_list - 4 + change_line],
        cells_list[cell_center.index_list - 4 + (change_line * 2)],
        cells_list[cell_center.index_list + 4 + change_line],
        cells_list[cell_center.index_list + 4 + (change_line * 2)],
        cells_list[cell_center.index_list - 1 + (change_line * 2)],
        cells_list[cell_center.index_list + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 2)],
    ]

    symbole_invaders_add: list[Cells] = [
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list - 1 - change_line],
    ]
    list_symbole.append(symbole_invaders)
    list_symbole.append(symbole_invaders_add)

    symbole_heart: list[Cells] = [
        cells_list[cell_center.index_list],
        cells_list[cell_center.index_list - 1],
        cells_list[cell_center.index_list - 2],
        cells_list[cell_center.index_list - 3],
        cells_list[cell_center.index_list - 4],
        cells_list[cell_center.index_list + 1],
        cells_list[cell_center.index_list + 2],
        cells_list[cell_center.index_list + 3],
        cells_list[cell_center.index_list + 4],
        cells_list[cell_center.index_list - change_line],
        cells_list[cell_center.index_list - (change_line * 2)],
        cells_list[cell_center.index_list + change_line],
        cells_list[cell_center.index_list + (change_line * 2)],
        cells_list[cell_center.index_list + (change_line * 3)],
        cells_list[cell_center.index_list + (change_line * 4)],
        cells_list[cell_center.index_list - 1 - change_line],
        cells_list[cell_center.index_list - 2 - change_line],
        cells_list[cell_center.index_list - 3 - change_line],
        cells_list[cell_center.index_list - 4 - change_line],
        cells_list[cell_center.index_list + 1 - change_line],
        cells_list[cell_center.index_list + 2 - change_line],
        cells_list[cell_center.index_list + 3 - change_line],
        cells_list[cell_center.index_list + 4 - change_line],
        cells_list[cell_center.index_list - 1 - (change_line * 2)],
        cells_list[cell_center.index_list - 2 - (change_line * 2)],
        cells_list[cell_center.index_list - 3 - (change_line * 2)],
        cells_list[cell_center.index_list - 4 - (change_line * 2)],
        cells_list[cell_center.index_list + 1 - (change_line * 2)],
        cells_list[cell_center.index_list + 2 - (change_line * 2)],
        cells_list[cell_center.index_list + 3 - (change_line * 2)],
        cells_list[cell_center.index_list + 4 - (change_line * 2)],
        cells_list[cell_center.index_list - 1 - (change_line * 3)],
        cells_list[cell_center.index_list - 2 - (change_line * 3)],
        cells_list[cell_center.index_list - 3 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 - (change_line * 3)],
        cells_list[cell_center.index_list + 2 - (change_line * 3)],
        cells_list[cell_center.index_list + 3 - (change_line * 3)],
        cells_list[cell_center.index_list + 1 + change_line],
        cells_list[cell_center.index_list + 2 + change_line],
        cells_list[cell_center.index_list + 3 + change_line],
        cells_list[cell_center.index_list - 1 + change_line],
        cells_list[cell_center.index_list - 2 + change_line],
        cells_list[cell_center.index_list - 3 + change_line],
        cells_list[cell_center.index_list - 1 + (change_line * 2)],
        cells_list[cell_center.index_list - 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 2)],
        cells_list[cell_center.index_list + 2 + (change_line * 2)],
        cells_list[cell_center.index_list + 1 + (change_line * 3)],
        cells_list[cell_center.index_list - 1 + (change_line * 3)],
    ]

    match symbole_index:
        case 0:
            for case in symbole_42:
                change_state(case, lab_str, True, False)
            change_wall_cell(cells_list, symbole_42, size_values)
        case 1:
            for case in symbole_invaders:
                change_state(case, lab_str, True, False)
            for case in symbole_invaders_add:
                change_state(case, lab_str, False, True)
            change_wall_cell(cells_list, symbole_invaders, size_values)
        case 2:
            for case in symbole_heart:
                change_state(case, lab_str, True, False)
            change_wall_cell(cells_list, symbole_heart, size_values)

    return symbole_42


def change_wall_cell(
    cells_list: list[Cells], symbol_lst: list[Cells], size_values: list[int]
) -> None:
    """
    Remove walls around symbol cells.

    The function updates the wall states of cells surrounding the selected
    symbol cells to create open passages in the maze.

    Args:
        cells_list: List of all cells composing the maze.
        symbol_lst: List of cells forming the symbol.
        size_values: Dimensions of the maze.

    Returns:
        None
    """
    change_line: int = (size_values[0] * 2) - 1

    for c in symbol_lst:
        cells_list[c.index_list - 1].walls["E"] = False
        cells_list[c.index_list + 1].walls["W"] = False
        cells_list[c.index_list - change_line].walls["S"] = False
        cells_list[c.index_list + change_line].walls["N"] = False
        cells_list[c.index_list - 2].walls["E"] = False
        cells_list[c.index_list + 2].walls["W"] = False
        cells_list[c.index_list - change_line * 2].walls["S"] = False
        cells_list[c.index_list + change_line * 2].walls["N"] = False


def symbol_logic(
    cells_list: list[Cells],
    size_values: list[int],
    lab_str: list[str],
    symbole_index: int,
) -> list[Cells]:
    """
    Apply the selected center symbol to the maze.

    The function acts as a wrapper around the center symbol generation logic
    and returns the cells modified by the symbol.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_str: List representing the current maze state.
        symbole_index: Index of the symbol to apply.

    Returns:
        A list of cells modified by the selected symbol.
    """
    return center_symbol(cells_list, size_values, lab_str, symbole_index)
