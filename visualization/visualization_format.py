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



