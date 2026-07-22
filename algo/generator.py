from .wall_destroyer import change_state
from classes import Cells
import random


def choice_direction(cell: Cells) -> str:
    is_ok: bool = False
    dir: str = ""
    while not is_ok:
        dir_list: list[str] = ["N", "W", "S", "E"]
        dir: str = dir_list[random.randint(0, len(dir_list) - 1)]
        if not cell.walls[dir]:
            print(f"{dir} pas dispo")
            continue
        is_ok = True

    return dir


def gen_maze(cells_list: list[Cells]) -> None:
    choice_direction(cells_list[0])
