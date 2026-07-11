def parse_size(file_name: str) -> list[int]:
    size: list[int] = [0, 0]
    allow_params: list[str] = ["WIDTH", "HEIGHT"]
    try:
        with open(file_name) as file:
            for line in file:
                line_clean = line.strip(" /n")
                splited_line: list[str] = line_clean.split("=")
                if splited_line[0] in allow_params:
                    if splited_line[0] == "WIDTH":
                        try:
                            size[0] = int(splited_line[1])
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            size[1] = int(splited_line[1])
                        except Exception as e:
                            print(e)
    except Exception as e:
        print(e)
    return size


if __name__ == "__main__":
    print(parse_size("config.txt"))
