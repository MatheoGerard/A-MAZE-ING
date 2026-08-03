from sys import argv
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
from rich import print as richprint
from typing import Any
from music import get_music_volume, get_music_state
from mazegen import Cells, parsing_config
import time


def music_player_print(is_play: bool, volume: float) -> Panel:
    """
    Create a panel displaying the current music player status.

    The function generates an ASCII representation of the music player,
    indicating whether playback is active or paused as well as the current
    volume level, then returns it as a Rich panel.

    Args:
        is_play: Indicates whether the music is currently playing.
        volume: The current music volume.

    Returns:
        A Rich panel containing the music player interface.
    """
    music_player: str = ""
    if not is_play:
        if round(volume, 1) == 0.0:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [     ] o
        P
    """
        if round(volume, 1) == 0.2:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [-    ] o
        P
    """
        if round(volume, 1) == 0.4:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [--   ] o
        P
    """
        if round(volume, 1) == 0.6:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [---  ] o
        P
    """
        if round(volume, 1) == 0.8:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [---- ] o
        P
    """
        if round(volume, 1) == 1.0:
            music_player = r"""
MUSIC_PLAYER:
        ▶︎       🕪  i [-----] o
        P
    """
    if is_play:
        if round(volume, 1) == 0.0:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [     ] o
        P
    """
        if round(volume, 1) == 0.2:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [-    ] o
        P
    """
        if round(volume, 1) == 0.4:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [--   ] o
        P
    """
        if round(volume, 1) == 0.6:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [---  ] o
        P
    """
        if round(volume, 1) == 0.8:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [---- ] o
        P
    """
        if round(volume, 1) == 1.0:
            music_player = r"""
MUSIC_PLAYER:
        ⏸       🕪  i [-----] o
        P
    """

    return Panel(music_player, expand=False, border_style="green")


def stat_print(stats: int) -> Panel:
    """
    Create a panel displaying maze statistics.

    The function reads the maze configuration and generates a Rich panel
    containing the maze dimensions and the number of moves required by the
    solution.

    Args:
        stats: The number of moves in the maze solution.

    Returns:
        A Rich panel containing the maze statistics.
    """
    data: dict[str, Any] = parsing_config(argv[1])
    stats_str: str = rf"""
STATISTIQUES:
    size: {data["WIDTH"]} X {data["HEIGHT"]}
    Soluce move: {stats}
    """
    return Panel(stats_str, expand=False, border_style="blue")


def visualizatoin_format(
    to_display: list[str],
    color_set: str,
    console: Console,
) -> None:
    """
    Render the formatted maze and related information in the console.

    The function converts the maze representation into colored blocks,
    displays the maze alongside the statistics and music player panels, and
    prints the legend for the selected color set.

    Args:
        to_display: List representing the maze to display.
        color_set: Color theme used to render the maze.
        console: The Rich console used to display the interface.

    Returns:
        None
    """
    colors: list[str] = color_set.split("-")
    move_nb: int = 0

    char_map: dict[str, str] = {
        "#": colors[0],
        " ": colors[1],
        ".": colors[2],
        "E": colors[3],
        "e": colors[4],
        "L": colors[5],
        "Y": colors[6],
        "S": colors[7],
        "P": "purple",
    }

    lab_str: str = "".join(to_display)
    txt_obj: Text = Text()

    for char in lab_str:
        if char == "\n":
            txt_obj.append("\n")
        elif char in char_map:
            txt_obj.append("██", style=char_map[char])
            if char == "S":
                move_nb += 1
        else:
            txt_obj.append(char)

    console.print(
        Columns(
            [
                Panel(txt_obj, expand=False, border_style="purple"),
                stat_print(move_nb + 1),
                music_player_print(get_music_state(), get_music_volume()),
            ]
        ),
    )
    legende_print(color_set)


def legende_print(color_set: str) -> None:
    """
    Display the maze legend with the corresponding colors.

    The function generates a legend showing the meaning of the different
    maze elements (entry, exit, and path) using the colors defined in the
    selected color set.

    Args:
        color_set: Color theme used to display the legend.

    Returns:
        None
    """
    colors: list[str] = color_set.split("-")

    char_map: dict[str, str] = {
        "#": colors[0],
        " ": colors[1],
        ".": colors[2],
        "E": colors[3],
        "e": colors[4],
        "L": colors[5],
        "Y": colors[6],
        "S": colors[7],
    }

    richprint(
        f"[{char_map['E']}]██[/{char_map['E']}] entry   "
        f"[{char_map['e']}]██[/{char_map['e']}] exit  "
        f"[{char_map['S']}]██[/{char_map['S']}] path"
    )


def title_print(console: Console) -> None:
    """
    Display the project title in the console.

    The function renders the ASCII title inside a Rich panel with a yellow
    border.

    Args:
        console: The Rich console used to display the title.

    Returns:
        None
    """
    title: str = r"""
_______       ______  ________________________   ____________   __________
___    |      ___   |/  /__    |__  /__  ____/   ____  _/__  | / /_  ____/
__  /| |________  /|_/ /__  /| |_  /__  __/_________  / __   |/ /_  / __
_  ___ |/_____/  /  / / _  ___ |  /__  /___/_____/_/ /  _  /|  / / /_/ /
/_/  |_|      /_/  /_/  /_/  |_/____/_____/      /___/  /_/ |_/  \____/
"""
    console.print(Panel(title, expand=False, border_style="yellow"))


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
    """
    Display the maze solution path.

    The function follows the solution steps from the entry cell, updates the
    maze representation by marking the solution path, and optionally displays
    the path creation as an animation.

    Args:
        entry: The starting cell of the maze.
        soluce: List containing the solution path directions.
        lab_lst: List representing the current maze state.
        cell_list: List of all cells composing the maze.
        size_values: Dimensions of the maze.
        color_set: Color theme used to display the maze.
        console: The Rich console used to render the maze.
        is_anim: Indicates whether the solution path should be displayed
            progressively.

    Returns:
        The updated maze representation containing the solution path.
    """
    change_line: int = (size_values[0] * 2) - 1
    current: Cells = entry

    for w in soluce[1:-1]:
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
            title_print(console)
            visualizatoin_format(lab_lst, color_set, console)
            time.sleep(0.0005)

    return lab_lst
