from typing import Any
import sys


def equal_count(line: str) -> int:
    """
    Count the number of equal signs in a string.

    The function iterates through the provided string and counts how many
    ``=`` characters it contains.

    Args:
        line: String to inspect.

    Returns:
        The number of equal signs found in the string.
    """
    equal_counter: int = 0
    for c in line:
        if c == "=":
            equal_counter += 1
    return equal_counter


def parsing_config(file_name: str) -> dict[str, Any]:
    """
    Parse a maze configuration file.

    The function reads the configuration file, ignores comments and empty
    lines, validates the format of each entry, and stores the resulting
    key-value pairs in a dictionary.

    Args:
        file_name: Name of the configuration file.

    Returns:
        A dictionary containing the parsed configuration values.
    """
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
    """
    Validate the required configuration parameters.

    The function checks that all mandatory configuration keys are present in
    the parsed configuration data.

    Args:
        data: Dictionary containing the parsed configuration values.

    Returns:
        None
    """
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
        if not data.get(params):
            raise ValueError(f"{params} must be not NONE")


def validate_size_value(data: dict[str, Any]) -> list[int]:
    """
    Extract the maze dimensions from the configuration.

    The function converts the width and height values into integers and
    returns them as a list.

    Args:
        data: Dictionary containing the parsed configuration values.

    Returns:
        A list containing the maze width and height.
    """
    size: list[int] = []
    try:
        size.append(int(data["WIDTH"]))
    except Exception:
        raise TypeError("WIDTH must be a int")
    try:
        size.append(int(data["HEIGHT"]))
    except Exception:
        raise TypeError("HEIGHT must be a int")

    if size[0] < 0:
        raise ValueError("WIDTH must be positive")
    if size[1] < 0:
        raise ValueError("HEIGHT must be positive")

    return size


def validate_entry_exit(data: dict[str, Any], size: list[int]) -> list[list[int]]:
    """
    Validate the maze entry and exit positions.

    The function checks that the entry and exit coordinates are correctly
    formatted, located inside the maze boundaries, and are not identical.
    The validated coordinates are converted to the internal maze format.

    Args:
        data: Dictionary containing the parsed configuration values.
        size: Dimensions of the maze.

    Returns:
        A list containing the converted entry and exit coordinates.
    """
    if data["ENTRY"] == data["EXIT"]:
        raise ValueError("Entry and exit in same place")

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

    return [
        [entry_point[0] * 2, entry_point[1] * 2],
        [exit_point[0] * 2, exit_point[1] * 2],
    ]


def validate_perfect(data: dict[str, Any]) -> bool:
    """
    Validate the perfect maze option.

    The function checks that the ``PERFECT`` value is either ``True`` or
    ``False`` and returns the corresponding boolean value.

    Args:
        data: Dictionary containing the parsed configuration values.

    Returns:
        ``True`` if a perfect maze should be generated, otherwise ``False``.
    """
    if data["PERFECT"] != "True" and data["PERFECT"] != "False":
        raise ValueError("PERFECT must be 'True' or 'False'")
    if data["PERFECT"] == "True":
        return True
    else:
        return False


def validate_output_name(data: dict[str, Any]) -> None:
    """
    Validate the output file name.

    The function verifies that the configured output file name matches the
    expected value.

    Args:
        data: Dictionary containing the parsed configuration values.

    Returns:
        None
    """
    if data["OUTPUT_FILE"] != "maze.txt":
        raise ValueError("OUTPUT_FILE must be maze.txt")


def seed_parsing(data: dict[str, Any]) -> None | str:
    """
    Parse the random generation seed.

    The function returns the configured seed if one is provided. Otherwise,
    it returns ``None``.

    Args:
        data: Dictionary containing the parsed configuration values.

    Returns:
        The seed as a string, or ``None`` if no seed is specified.
    """
    if data["SEED"] == "":
        return None
    else:
        return str(data["SEED"])


def return_parsed_values() -> dict[str, Any]:
    """
    Parse the configuration file passed as a command-line argument.

    The function reads the configuration file specified in ``sys.argv`` and
    returns the parsed configuration values.

    Returns:
        A dictionary containing the parsed configuration values.
    """
    return parsing_config(sys.argv[1])


if __name__ == "__main__":
    try:
        parse_data: dict[str, Any] = parsing_config("../config.txt")
        validate_config(parse_data)
        size_values: list[int] = validate_size_value(parse_data)
        validate_entry_exit(parse_data, size_values)
        validate_perfect(parse_data)
        validate_output_name(parse_data)
        print("MAZE GENERATE")
    except Exception as e:
        print(e)
