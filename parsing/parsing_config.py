def parse_size(file_name: str) -> list[int]:
    size: list[int] = [0, 0]
    allow_params: list[str] = ["WIDTH", "HEIGHT"]
    with open(file_name) as file:
        for line in file:
            line_clean = line.strip(" /n")
            splited_line: list[str] = line_clean.split("=")
            if splited_line[0] in allow_params:
                value: int | None = None
                if splited_line[0] == "WIDTH":
                    value = int(splited_line[1])
                    if value >= 0:
                        size[0] = value
                    else:
                        raise ValueError("width is negative!")
                else:
                    value = int(splited_line[1])
                    if value >= 0:
                        size[1] = value
                    else:
                        raise ValueError("HEIGHT is negative!")
    return size


if __name__ == "__main__":
    print(parse_size("config.txt"))
