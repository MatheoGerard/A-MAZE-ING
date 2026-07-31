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


def legende_print(color_set: str) -> None:
    colors: list[str] = color_set.split("-")

    char_map: dict[str, str] = {
        "#": colors[0],
        " ": colors[1],
        ".": colors[2],
        "E": "green",
        "e": "purple",
        "L": "blue",
        "Y": "white",
        "S": "red",
    }

    print(f"[{char_map['E']}]██[/{char_map['E']}] entry        ")
