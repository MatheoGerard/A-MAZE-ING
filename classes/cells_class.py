class Cells:
    def __init__(self, is_wall: bool, x: int, y: int) -> None:
        self.char: str = ""
        self.set_char(is_wall)
        self.position: list[int] = []
        self.set_position(x, y)

    def set_char(self, is_wall: bool) -> None:
        if is_wall:
            self.char += "#"
        else:
            self.char += " "

    def set_position(self, x: int, y: int) -> None:
        if not isinstance(x, int):
            raise TypeError("x must be a int")
        if not isinstance(y, int):
            raise TypeError("y must be a int")

        self.position.append(x)
        self.position.append(y)
