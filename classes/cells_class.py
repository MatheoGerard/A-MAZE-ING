class Cells:
    def __init__(
        self,
        is_wall: bool,
        index: int,
        x: int,
        y: int,
        is_entry: bool = False,
        is_exit: bool = False,
    ) -> None:
        self.char: str = ""
        self.set_char(is_wall)
        self.position: list[int] = []
        self.set_position(x, y)
        self.is_entry: bool = is_entry
        self.is_exit: bool = is_exit
        self.is_used: bool = False
        self.ways: int = 15
        self.index_str: int = index

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


#    def define_ways(self) -> None:
#       if self.position[0] == 0:
