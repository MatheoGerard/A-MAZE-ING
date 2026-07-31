from os import pathconf_names
import sys
import random
from rich import print
from rich.console import Console
from rich.panel import Panel
from algo.generator import unperfect
import parsing
from classes import Cells
from typing import Any
import algo
import solver
import visualization as visu

console = Console()


def title_print() -> None:
    title: str = r"""
 ______                     ______  ________   ____            ______   __  __  ____
/\  _  \            /'\_/`\/\  _  \/\_____  \ /\  _`\         /\__  _\ /\ \/\ \/\  _`\
\ \ \L\ \          /\      \ \ \L\ \/____//'/'\ \ \L\_\       \/_/\ \/ \ \ `\\ \ \ \L\_\
 \ \  __ \  _______\ \ \__\ \ \  __ \   //'/'  \ \  _\L   _______\ \ \  \ \ , ` \ \ \L_L
  \ \ \/\ \/\______\\ \ \_/\ \ \ \/\ \ //'/'___ \ \ \L\ \/\______\\_\ \__\ \ \`\ \ \ \/, \
   \ \_\ \_\/______/ \ \_\\ \_\ \_\ \_\/\_______\\ \____/\/______//\_____\\ \_\ \_\ \____/
    \/_/\/_/          \/_/ \/_/\/_/\/_/\/_______/ \/___/          \/_____/ \/_/\/_/\/___/

"""
    console.print(Panel(title, expand=False, border_style="yellow"))


def input_panel() -> None:
    inputs: str = "Change color: 0\nChange center: 1\nRegenerate maze: 2\nDisplay soluce: 3\nAnim mode: 4\nExit: 9"
    input_panel = Panel(inputs, expand=False, border_style="green")
    console.print(input_panel)


def draw_lab_size(
    size: list[int], entry_val: list[int], exit_val: list[int]
) -> tuple[str, list[Cells]]:
    cells_list: list[Cells] = []
    buffer: str = ""
    width_total: int = size[0] * 2
    height_total: int = (size[1] * 2) + 2

    range_width = range(0, width_total)
    range_height = range(0, height_total - 1)

    is_finish: bool = False

    while not is_finish:
        for x in range_height:
            buffer += "."
            if x == 0:
                for _ in range_width:
                    buffer += "."
                buffer += "\n"
                continue

            if x == height_total - 2:
                for _ in range_width:
                    buffer += "."
                buffer += "\n"
                continue

            if x % 2 == 0:
                for j in range_width:
                    if j == width_total - 1:
                        buffer += "."
                        break
                    new_cell: Cells = Cells(True, len(buffer), j, x - 1, size)
                    if new_cell.position == entry_val:
                        new_cell.char = "E"
                        new_cell.is_entry = True
                    elif new_cell.position == exit_val:
                        new_cell.char = "e"
                        new_cell.is_exit = True
                    cells_list.append(new_cell)
                    buffer += new_cell.char
            else:
                for y in range_width:
                    if y == width_total - 1:
                        buffer += "."
                        break
                    if y % 2 != 0:
                        new_cell: Cells = Cells(True, len(buffer), y, x - 1, size)
                        if new_cell.position == entry_val:
                            new_cell.char = "E"
                            new_cell.is_entry = True
                        elif new_cell.position == exit_val:
                            new_cell.char = "e"
                            new_cell.is_exit = True
                        cells_list.append(new_cell)
                        buffer += new_cell.char
                    else:
                        new_cell: Cells = Cells(False, len(buffer), y, x - 1, size)
                        if new_cell.position == entry_val:
                            new_cell.char = "E"
                            new_cell.is_entry = True
                        elif new_cell.position == exit_val:
                            new_cell.char = "e"
                            new_cell.is_exit = True
                        cells_list.append(new_cell)
                        buffer += new_cell.char

            buffer += "\n"
        is_finish = True

    return (buffer, cells_list)


def set_cells_index(cells_list: list[Cells]) -> None:
    index: int = 0

    for c in cells_list:
        c.index_list = index
        index += 1


def entry_exit_in_symbol(entry_exit: list[list[int]], cells_list: list[Cells]) -> None:
    for c in cells_list:
        if c.position == entry_exit[0]:
            raise ValueError("Entry in middle symbol")
        elif c.position == entry_exit[1]:
            raise ValueError("Exit in middle symbol")


def init_lab(
    index: int, color_set: list[str], symbol_index: int
) -> tuple[list[str], list[Cells | str], list[Cells], list[int]]:
    parse_data: dict[str, Any] = parsing.parsing_config(sys.argv[1])
    parsing.validate_config(parse_data)
    size_values: list[int] = parsing.validate_size_value(parse_data)
    entry_exit: list[list[int]] = parsing.validate_entry_exit(parse_data, size_values)
    perfect: bool = parsing.validate_perfect(parse_data)
    parsing.validate_output_name(parse_data)
    seed: None | str = parsing.seed_parsing(parse_data)
    if seed:
        random.seed(seed)
    console.clear()
    lab_data: tuple[str, list[Cells]] = draw_lab_size(
        size_values, entry_exit[0], entry_exit[1]
    )
    lab_data_str: str = lab_data[0]
    active_cell: list[Cells] = lab_data[1]
    set_cells_index(active_cell)
    lab_data_lst: list[str] = list(lab_data_str)
    if size_values[0] > 8 and size_values[1] > 6:
        symbol_lst: list[Cells] = algo.symbol_logic(
            active_cell, size_values, lab_data_lst, symbol_index
        )
    else:
        print("[red]Not enough space for 42 symbol![/red]")
    lab_data_lst = algo.gen_maze(active_cell, size_values, lab_data_lst)
    if not perfect:
        unperfect(active_cell, size_values, lab_data_lst)
    soluce: list[Cells | str] = solver.bfs_function(active_cell, size_values)
    algo.hex_trad(
        active_cell,
        size_values,
        parse_data["OUTPUT_FILE"],
        parse_data["ENTRY"],
        parse_data["EXIT"],
        soluce,
    )
    if size_values[0] > 8 and size_values[1] > 6:
        entry_exit_in_symbol(entry_exit, symbol_lst)

    return lab_data_lst, soluce, active_cell, size_values


def loop_gameplay() -> None:
    color_set: list[str] = [

        "red-orange1-gold1-yellow1-chartreuse1-green1-cyan1-blue1",
        "grey15-grey35-grey58-grey78-white-steel_blue1-orchid1-deep_pink2",
        "deep_sky_blue1-steel_blue1-cyan1-medium_spring_green-chartreuse1-gold1-dark_orange-red1",
        "purple-blue_violet-royal_blue1-cornflower_blue-steel_blue1-sky_blue1-light_sky_blue1-white",
        "deep_pink2-hot_pink-orchid1-plum1-medium_orchid1-violet-thistle1-white",
        "dark_red-red3-orange3-gold3-yellow3-chartreuse3-green3-dark_green",
        "grey3-grey23-grey42-grey62-grey82-grey93-white-black",
        "navy_blue-deep_sky_blue4-deep_sky_blue1-cyan1-medium_spring_green-green1-chartreuse1-yellow1",
        # "purple-orchid-blue",
        # "bright_red-grey0-bright_blue",
        # "grey3-grey46-grey85",
        # "deep_pink1-plum1-deep_pink3-",
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

    is_soluce_print: bool = True

    last_gen, soluce, active_cells, size_values = init_lab(
        color_index, color_set, symbol_index
    )

    lab_data_cpy: list[str] = last_gen.copy()
    last_gen_soluce = solver.solver_print(
        solver.find_start(active_cells),
        soluce,
        lab_data_cpy,
        active_cells,
        size_values,
        color_set[color_index],
        console,
        False,
    )

    title_print()
    visu.visualizatoin_format(last_gen_soluce, color_set[color_index], console)
    visu.legende_print(color_set[color_index])
    input_panel()
    while not is_exit:
        key: str = input("Input: ")
        match key:
            case "9":
                is_exit = True
                print("Exit...")
            case "1":
                symbol_index = algo.change_symbole(symbol_index, symbol_nb)
                console.clear()
                last_gen, soluce, active_cells, size_values = init_lab(
                    color_index, color_set, symbol_index
                )
                lab_data_cpy: list[str] = last_gen.copy()
                last_gen_soluce = solver.solver_print(
                    solver.find_start(active_cells),
                    soluce,
                    lab_data_cpy,
                    active_cells,
                    size_values,
                    color_set[color_index],
                    console,
                    False,
                )
                title_print()
                if not is_soluce_print:
                    visu.visualizatoin_format(last_gen, color_set[color_index], console)
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "2":
                console.clear()
                last_gen, soluce, active_cells, size_values = init_lab(
                    color_index, color_set, symbol_index
                )
                lab_data_cpy: list[str] = last_gen.copy()
                last_gen_soluce = solver.solver_print(
                    solver.find_start(active_cells),
                    soluce,
                    lab_data_cpy,
                    active_cells,
                    size_values,
                    color_set[color_index],
                    console,
                    False,
                )
                title_print()
                if not is_soluce_print:
                    visu.visualizatoin_format(last_gen, color_set[color_index], console)
                else:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                input_panel()
            case "3":
                console.clear()
                title_print()
                if not is_soluce_print:
                    visu.visualizatoin_format(
                        last_gen_soluce, color_set[color_index], console
                    )
                    is_soluce_print = True
                else:
                    visu.visualizatoin_format(last_gen, color_set[color_index], console)
                    is_soluce_print = False
                input_panel()
            case "4":
                console.clear()
                lab_data_cpy = last_gen.copy()
                title_print()
                last_gen_soluce = solver.solver_print(
                    solver.find_start(active_cells),
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
            case "0":
                if color_index == len(color_set) - 1:
                    color_index = 0
                else:
                    color_index += 1
                console.clear()
                title_print()
                if not is_soluce_print:
                    visu.visualizatoin_format(last_gen, color_set[color_index], console)
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
    except KeyboardInterrupt as e:
        print("[red]\nEnded by user[/red]")
