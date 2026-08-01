from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from rich import print


def visualizatoin_format(
    to_display: list[str],
    color_set: str,
    console: Console,
) -> None:
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
        "P": "purple",
    }

    lab_str: str = "".join(to_display)
    txt_obj: Text = Text()

    for char in lab_str:
        if char == "\n":
            txt_obj.append("\n")
        elif char in char_map:
            txt_obj.append("██", style=char_map[char])
        else:
            txt_obj.append(char)
    my_panel = Panel(txt_obj, expand=False, border_style="purple")
    console.print(my_panel)
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

    print(
        f"[{char_map['E']}]██[/{char_map['E']}] entry   [{char_map['e']}]██[/{char_map['e']}] exit  [{char_map['S']}]██[/{char_map['S']}] path"
    )


def title_print(console: Console) -> None:
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
