from enum import Enum
from typing import Any

import inquirer

from file_generator.random_file_generator import FileGenerator


class ProgramAction(Enum):
    run_program = "Run Program"
    generate_random_files = "Generate Random Files"

    @classmethod
    def list(cls) -> list[Any]:
        return list(map(lambda c: c.value, cls))


if __name__ == "__main__":
    questions = [
        inquirer.List(
            "action",
            message="Select action:",
            choices=ProgramAction.list(),
        ),
    ]
    answers = inquirer.prompt(questions)

    match answers["action"]:
        case ProgramAction.run_program.value:
            print("Run P")
        # case ProgramAction.run_tests.value:
        #     run_tests()
        case ProgramAction.generate_random_files.value:
            FileGenerator().run_random_file_generation()
