from mazegen import find_start, find_finish, Cells
from .input_reader import go_north, go_east, go_south, go_west, input_read
from visualization import visualizatoin_format as visu
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from visualization import title_print


def print_input(console: Console) -> None:
    """
    Display the available keyboard controls in the console.

    The function prints a set of panels showing the keys used for movement
    (W, A, S, D) and the key to quit the application.

    Args:
        console: The Rich console used to render the controls.

    Returns:
        None
    """
    console.print(
        Columns(
            [
                Panel("w ↑", expand=False),
                Panel("s ↓", expand=False),
                Panel("d →", expand=False),
                Panel("a ←", expand=False),
                Panel("q QUIT", expand=False),
            ]
        ),
    )


def game_fucntion(
    cells_list: list[Cells],
    size_values: list[int],
    lab_lst: list[str],
    color_set: str,
    console: Console,
) -> None:
    """
    Run the main game loop.

    The function initializes the player and exit positions, displays the maze,
    and continuously reads keyboard input to move the player until the exit is
    reached or the user chooses to quit.

    Args:
        cells_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        lab_lst: List representing the current maze state.
        color_set: Color theme used to display the maze.
        console: The Rich console used to render the game.

    Returns:
        None
    """
    is_win: bool = False
    key: str = ""
    current: Cells = find_start(cells_list)
    exit_cell: Cells = find_finish(cells_list)

    console.clear()
    print("\033[H", end="")
    title_print(console)
    visu(lab_lst, color_set, console)
    print_input(console)
    while not is_win:
        key = input_read()

        match key:
            case "w":
                current = go_north(current, cells_list, size_values, lab_lst)
                print("\033[H", end="")
                title_print(console)
                visu(lab_lst, color_set, console)
                print_input(console)
            case "s":
                current = go_south(current, cells_list, size_values, lab_lst)
                print("\033[H", end="")
                title_print(console)
                visu(lab_lst, color_set, console)
                print_input(console)
            case "d":
                current = go_east(current, cells_list, size_values, lab_lst)
                print("\033[H", end="")
                title_print(console)
                visu(lab_lst, color_set, console)
                print_input(console)
            case "a":
                current = go_west(current, cells_list, size_values, lab_lst)
                print("\033[H", end="")
                title_print(console)
                visu(lab_lst, color_set, console)
                print_input(console)
            case "q":
                is_win = True
                current.char = "e"
                lab_lst[current.index_str] = "e"
                break
            case _:
                print("\033[H", end="")
                title_print(console)
                visu(lab_lst, color_set, console)
                print_input(console)
                print("Not a correct direction! (use 'w', 'a', 's', 'd')")
                print_input(console)

        if (
            current.position[0] == exit_cell.position[0]
            and current.position[1] == exit_cell.position[1]
        ):
            is_win = True
            current.char = "e"
            lab_lst[current.index_str] = "e"
