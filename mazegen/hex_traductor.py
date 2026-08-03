from .cells_class import Cells


def hex_trad(
    cell_lst: list[Cells],
    size_values: list[int],
    file_name: str,
    entry: str,
    exit_value: str,
    soluce: list[Cells | str],
) -> None:
    change_line: int = (size_values[0] * 2) - 1

    for c in cell_lst:
        if c.position[0] != 0:
            if (
                cell_lst[c.index_list - 1].char == " "
                or cell_lst[c.index_list - 1].char == "E"
                or cell_lst[c.index_list - 1].char == "e"
            ):
                c.ways -= 8
        if c.position[0] != (size_values[0] * 2) - 2:
            if (
                cell_lst[c.index_list + 1].char == " "
                or cell_lst[c.index_list + 1].char == "E"
                or cell_lst[c.index_list + 1].char == "e"
            ):
                c.ways -= 2
        if c.position[1] != 0:
            if (
                cell_lst[c.index_list - change_line].char == " "
                or cell_lst[c.index_list - change_line].char == "E"
                or cell_lst[c.index_list - change_line].char == "e"
            ):
                c.ways -= 1
        if c.position[1] != (size_values[1] * 2) - 2:
            if (
                cell_lst[c.index_list + change_line].char == " "
                or cell_lst[c.index_list + change_line].char == "E"
                or cell_lst[c.index_list + change_line].char == "e"
            ):
                c.ways -= 4

    output_file_generator(
        cell_lst, size_values, file_name, entry, exit_value, soluce
    )


def output_file_generator(
    cell_lst: list[Cells],
    size_values: list[int],
    file_name: str,
    entry: str,
    exit_value: str,
    soluce: list[Cells | str],
) -> None:
    str_list: list[str] = []
    open(file_name, "w").close()
    with open(file_name, "a") as file:
        for c in cell_lst:
            if c.position[0] % 2 == 0 and c.position[1] % 2 == 0:
                list_hex_value: list[str] = list(hex(c.ways))
                hex_to_str: str = "".join(list_hex_value[2:])
                file.write(hex_to_str)
                if c.position[0] == (size_values[0] * 2) - 2:
                    file.write("\n")
        file.write("\n")
        file.write(entry)
        file.write("\n")
        file.write(exit_value)
        file.write("\n")
        for x in soluce[1:]:
            if isinstance(x, str):
                str_list.append(x)
        file.write("".join(str_list))
