from typing import Any
from mazegen import init_lab, Cells


class MazeGenerator:
    def __init__(
        self,
        width: int | None,
        height: int | None,
        entry_value: str | None,
        exit_value: str | None,
        output_file: str | None = "maze.txt",
        perfect: str | None = "False",
        seed: str | None = None,
        symbole: int = 0,
    ) -> None:
        """
        Initialize a maze generator instance.

        The constructor stores all maze generation parameters, initializes the
        internal data structures, and immediately starts the maze generation
        process.

        Args:
            width: Width of the maze.
            height: Height of the maze.
            entry_value: Coordinates of the maze entry. "x, y"
            exit_value: Coordinates of the maze exit. "x, y"
            output_file: Name of the output file.
            perfect: Whether to generate a perfect maze.
            seed: Seed used for random generation.
            symbole: Character set identifier used to render the maze.

        Returns:
            None
        """
        self.data: dict[str, Any] = {
            "WIDTH": width,
            "HEIGHT": height,
            "ENTRY": entry_value,
            "EXIT": exit_value,
            "OUTPUT_FILE": output_file,
            "PERFECT": perfect,
            "SEED": seed,
        }
        self.lab_format_lst: list[str] = []
        self.soluce_lst: list[Cells | str] = []
        self.cells_lst: list[Cells] = []
        self.size: list[int] = []
        self.symbole: int = symbole
        self.generator()

    def generator(self) -> None:
        """
        Generate the maze.

        The function initializes the maze structure, creates the internal cell
        representation, and prepares all data required for solving and
        exporting the maze.

        Returns:
            None
        """
        (
            self.lab_format_lst,
            self.soluce_lst,
            self.cells_lst,
            self.size,
        ) = init_lab(self.symbole, self.data)
