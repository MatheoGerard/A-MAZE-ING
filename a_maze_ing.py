import readchar
from rich import print
from rich.console import Console
from rich.panel import Panel
from music.music_manager import music_pause
from typing import Any
import visualization as visu
from gameplay import game_fucntion
import music
from mazegen import init_lab, find_start, return_parsed_values, change_symbole, Cells, find_start, MazeGenerator

console = Console()


def input_panel() -> None:
    inputs: str = (
        "Change color: 0\nChange center: 1"
        "\nRegenerate maze: 2"
        "\nDisplay soluce: 3"
        "\nAnim mode: 4"
        "\nGame mode: 5"
        "\nExit: 9"
    )
    input_panel = Panel(inputs, expand=False, border_style="green")
    console.print(input_panel)


def loop_gameplay() -> None:
    console.clear()
    data: dict[str, Any] = return_parsed_values()
    music.music_player()
    color_set: list[str] = [
        "red-gold1-orange1-yellow1-chartreuse1-deep_pink2-cyan1-dark_orange3",
        "grey15-grey35-grey58-grey78-white-steel_blue1-orchid1-deep_pink2",
        "deep_sky_blue1-steel_blue1-cyan1-medium_spring_green-chartreuse1"
        "-gold1-dark_orange-red1",
        "purple-blue_violet-royal_blue1-cornflower_blue-steel_blue1-"
        "sky_blue1-light_sky_blue1-white",
        "deep_pink2-hot_pink-orchid1-plum1-medium_orchid1-violet"
        "-thistle1-white",
        "dark_red-red3-orange3-gold3-yellow3-chartreuse3-green3-dark_green",
        "grey3-grey23-grey42-grey62-grey82-grey93-white-grey1",
        "navy_blue-deep_sky_blue4-deep_sky_blue1-cyan1-medium_spring_green"
        "-green1-chartreuse1-yellow1",
    ]

    is_exit: bool = False
    color_index: int = 0
    symbol_index: int = 0
    symbol_nb: int = 3
    last_gen: list[str] = []
    soluce: list[Cells | str] = []
    last_gen_soluce: list[str] = []
    active_cells: list[Cells] = []
    size_values: list[int] = []

    is_music_pause: bool = False
    volume: float = 0.6
    music.music_set_volume(volume)

    is_soluce_print: bool = True

    maze = MazeGenerator(data["WIDTH"], data["HEIGHT"], data["ENTRY"], data["EXIT"], data["OUTPUT_FILE"], data["PERFECT"], data["SEED"], 1)

    # last_gen, soluce, active_cells, size_values = init_lab(
    #     color_index, color_set, symbol_index, data
    # )

    last_gen = maze.lab_format_lst
    soluce = maze.soluce_lst
    active_cells = maze.cells_lst
    size_values = maze.size

    lab_data_cpy: list[str] = last_gen.copy()
    last_gen_soluce = visu.solver_print(
        find_start(active_cells),
        soluce,
        lab_data_cpy,
        active_cells,
        size_values,
        color_set[color_index],
        console,
        False,
    )

    visu.title_print(console)
    visu.visualizatoin_format(last_gen_soluce, color_set[color_index], console)
    input_panel()
    while not is_exit:
        key: str = readchar.readkey()
        match key:
            case "9":
                is_exit = True
                print("Exit...")
            case "1":
                symbol_index = change_symbole(symbol_index, symbol_nb)
                console.clear()
                last_gen, soluce, active_cells, size_values = init_lab(
                    symbol_index, data
                )
                lab_data_cpy = last_gen.copy()
                last_gen_soluce = visu.solver_print(
                    find_start(active_cells),
                    soluce,
                    lab_data_cpy,
                    active_cells,
                    size_values,
                    color_set[color_index],
                    console,
                    False,
                )
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "2":
                console.clear()
                last_gen, soluce, active_cells, size_values = init_lab(
                    symbol_index, data
                )
                lab_data_cpy = last_gen.copy()
                last_gen_soluce = visu.solver_print(
                    find_start(active_cells),
                    soluce,
                    lab_data_cpy,
                    active_cells,
                    size_values,
                    color_set[color_index],
                    console,
                    False,
                )
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "3":
                console.clear()
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                    is_soluce_print = True
                else:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                    is_soluce_print = False
                input_panel()
            case "4":
                console.clear()
                lab_data_cpy = last_gen.copy()
                visu.title_print(console)
                last_gen_soluce = visu.solver_print(
                    find_start(active_cells),
                    soluce,
                    lab_data_cpy,
                    active_cells,
                    size_values,
                    color_set[color_index],
                    console,
                    True,
                )
                lab_data_cpy = last_gen.copy()
                input_panel()
                is_soluce_print = True
            case "5":
                lab_data_cpy = last_gen.copy()
                game_fucntion(
                    active_cells,
                    size_values,
                    lab_data_cpy,
                    color_set[color_index],
                    console,
                )
                console.clear()
                visu.title_print(console)
                visu.visualizatoin_format(
                    last_gen_soluce, color_set[color_index], console
                )
                input_panel()
            case "p":
                is_music_pause = music_pause(is_music_pause)
                console.clear()
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "o":
                volume = music.music_set_volume_up(volume)
                console.clear()
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "i":
                volume = music.music_set_volume_down(volume)
                console.clear()
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "0":
                if color_index == len(color_set) - 1:
                    color_index = 0
                else:
                    color_index += 1
                console.clear()
                visu.title_print(console)
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen, color_set[color_index], console
                    )
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case _:
                print("This choice is not supported!")


if __name__ == "__main__":
    try:
        loop_gameplay()
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("[red]\nEnded by user[/red]")
