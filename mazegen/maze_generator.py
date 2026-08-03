from typing import Any
from mazegen import init_lab, Cells


class MazeGenerator:
    def __init__(
        self,
        width: int,
        height: int,
        entry_value: list[int],
        exit_value: list[int],
        output_file: str,
        perfect: bool,
        seed: str | None = None,
        symbole: int = 0,
    ) -> None:
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
        self.lab_format_lst, self.soluce_lst, self.cells_lst, self.size  = init_lab(self.symbole, self.data)
