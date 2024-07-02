from enum import Enum, auto

program_modes_lookup_table: dict[str, str] = {
    "COMPARE_DIRS": "Compare Directories",
    "MOVE_DUPLICATES": "Move Duplicates to New Directory",
}


class ProgramModes(Enum):
    COMPARE_DIRS = auto()
    MOVE_DUPLICATES = auto()

    def __str__(self) -> str:
        return program_modes_lookup_table[self.name]
