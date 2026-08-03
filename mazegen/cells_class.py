class Cells:
    """
    Represent a single cell of the maze.

    A cell stores its position, type (wall or path), neighboring walls,
    indexes used for maze representation, and its state during maze solving
    and generation.

    Attributes:
        char: Character used to represent the cell in the maze display.
        position: Coordinates of the cell in the maze grid.
        is_entry: Indicates whether the cell is the maze starting point.
        is_exit: Indicates whether the cell is the maze exit.
        is_used: Indicates whether the cell has been visited or used.
        ways: Bitmask representing possible connections with neighboring cells.
        walls: Dictionary indicating the presence of walls in each direction.
        index_str: Index of the cell in the string representation of the maze.
        index_list: Index of the cell in the cell list.
        is_solved: Indicates whether the cell has been explored by the solver.

    Args:
        is_wall: Indicates whether the cell is a wall.
        index: Index of the cell in the maze representation.
        x: Horizontal coordinate of the cell.
        y: Vertical coordinate of the cell.
        size: Dimensions of the maze.
        is_entry: Whether this cell is the maze entry point.
        is_exit: Whether this cell is the maze exit point.
    """

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
        """
        Initialize a maze cell.

        The constructor creates a cell, sets its display character, defines its
        position, initializes its state flags, and configures the walls depending
        on whether the cell is a wall or its location in the maze.

        Args:
            is_wall: Indicates whether the cell represents a wall.
            index: Index of the cell in the maze string representation.
            x: Horizontal coordinate of the cell.
            y: Vertical coordinate of the cell.
            size: Dimensions of the maze.
            is_entry: Indicates whether the cell is the maze starting point.
            is_exit: Indicates whether the cell is the maze exit point.

        Returns:
            None
        """
        self.char: str = ""
        self.set_char(is_wall)
        self.position: list[int] = []
        self.set_position(x, y)
        self.is_entry: bool = is_entry
        self.is_exit: bool = is_exit
        self.is_used: bool = False
        self.ways: int = 15
        self.walls: dict[str, bool] = {
            "N": True,
            "E": True,
            "S": True,
            "W": True,
        }
        self.index_str: int = index
        self.index_list: int = 0
        self.define_walls(is_wall, size)
        self.is_used = False
        self.is_solved = False

    def set_char(self, is_wall: bool) -> None:
        """
        Set the display character of the cell.

        The function assigns a wall character if the cell is a wall, otherwise it
        assigns an empty space character for a walkable cell.

        Args:
            is_wall: Indicates whether the cell is a wall.

        Returns:
            None
        """
        if is_wall:
            self.char += "#"
        else:
            self.char += " "

    def set_position(self, x: int, y: int) -> None:
        """
        Set the coordinates of the cell.

        The function validates that the provided coordinates are integers and then
        stores them as the cell position.

        Args:
            x: Horizontal coordinate of the cell.
            y: Vertical coordinate of the cell.

        Raises:
            TypeError: If either coordinate is not an integer.

        Returns:
            None
        """
        if not isinstance(x, int):
            raise TypeError("x must be a int")
        if not isinstance(y, int):
            raise TypeError("y must be a int")

        self.position.append(x)
        self.position.append(y)

    def define_walls(self, is_wall: bool, size: list[int]) -> None:
        """
        Define the available walls of the cell.

        The function initializes the wall states of the cell. Wall cells have all
        directions disabled, while walkable cells have their borders disabled when
        they are located on the edge of the maze.

        Args:
            is_wall: Indicates whether the cell is a wall.
            size: Dimensions of the maze.

        Returns:
            None
        """
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
