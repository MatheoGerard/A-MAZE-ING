from .cells_class import Cells


def change_state(
    cell: Cells, lab_lst: list[str], is_symbole: bool, is_symbole_add: bool
) -> None:
    """
    Change the state of a maze cell.

    The function updates the character of a cell and its corresponding entry
    in the maze representation depending on whether the cell is part of a
    symbol, an additional symbol element, or a regular passage.

    Args:
        cell: Cell whose state needs to be modified.
        lab_lst: List representing the current maze state.
        is_symbole: Indicates whether the cell belongs to the main symbol.
        is_symbole_add: Indicates whether the cell belongs to an additional
            symbol element.

    Returns:
        None
    """
    if is_symbole:
        lab_lst[cell.index_str] = "L"
        cell.char = "L"
    elif is_symbole_add:
        lab_lst[cell.index_str] = "Y"
        cell.char = "Y"
    elif cell.char == "#":
        lab_lst[cell.index_str] = " "
        cell.char = " "
