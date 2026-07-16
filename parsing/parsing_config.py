from typing import Any


def equal_count(line: str) -> int:
    equal_counter: int = 0
    for c in line:
        if c == "=":
            equal_counter += 1
    return equal_counter


def parsing_config(file_name: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    with open(file_name) as file:
        for line in file:
            line_without_space: str = line.strip(" ")
            if line_without_space.startswith("#") or line_without_space.startswith(
                "\n"
            ):
                continue
            line_clean: str = line_without_space.strip("\n")
            if equal_count(line_without_space) != 1:
                raise ValueError(f"{line_clean} is not in correct format")
            splitted: list[str] = line_clean.split("=")
            data.update({splitted[0]: splitted[1]})
    return data


def validate_config(data: dict[str, Any]) -> None:
    mandatory: list[str] = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
    ]

    for params in mandatory:
        if params not in data.keys():
            raise ValueError(f"{params} not found")


def validate_size_value(data: dict[str, Any]) -> list[int]:
    size: list[int] = []
    size.append(int(data["WIDTH"]))
    size.append(int(data["HEIGHT"]))
    return size


def validate_entry_exit(data: dict[str, Any], size: list[int]) -> None:
    entry_point: list[int] = []
    if "," not in data["ENTRY"]:
        raise ValueError("wrong data format for ENTRY point")
    entry_split: list[str] = data["ENTRY"].split(",")
    if len(entry_split) != 2:
        raise ValueError("wrong data format for ENTRY point")
    for val in entry_split:
        entry_point.append(int(val))
    if entry_point[0] < 0 or entry_point[0] > size[0] - 1:
        raise ValueError("Entry width not in maze!")
    if entry_point[1] < 0 or entry_point[1] > size[1] - 1:
        raise ValueError("Entry height not in maze!")

    exit_point: list[int] = []
    exit_split: list[str] = data["EXIT"].split(",")
    if len(exit_split) != 2:
        raise ValueError("wrong data format for Exit point")
    for val in exit_split:
        exit_point.append(int(val))
    if exit_point[0] < 0 or exit_point[0] > size[0] - 1:
        raise ValueError("Exit width not in maze!")
    if exit_point[1] < 0 or exit_point[1] > size[1] - 1:
        raise ValueError("Exit height not in maze!")


if __name__ == "__main__":
    try:
        parse_data: dict[str, Any] = parsing_config("../config.txt")
        print(validate_config(parse_data))
        size_values: list[int] = validate_size_value(parse_data)
        validate_entry_exit(parse_data, size_values)
    except Exception as e:
        print(e)
