class Cells:
    def __init__(
        self,
        is_wall: bool,
        index: int,
        x: int,
        y: int,
        size: list[int],
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
        self.walls: dict[str, bool] = {"N": True, "E": True, "S": True, "W": True}
        self.index_str: int = index
        self.index_list: int = 0
        self.define_walls(is_wall, size)

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

    def define_walls(self, is_wall: bool, size: list[int]) -> None:
        if is_wall:
            for dir in self.walls:
                self.walls[dir] = False
        else:
            if self.position[1] == 0:
                self.walls["N"] = False
            if self.position[0] == 0:
                self.walls["W"] = False
            if self.position[1] == size[1] + size[1] - 2:
                self.walls["S"] = False
            if self.position[0] == size[0] + (size[0] - 2):
                self.walls["E"] = False
