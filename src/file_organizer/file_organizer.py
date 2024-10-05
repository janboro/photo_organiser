import filecmp
import os

import inquirer

from data_types.program_modes_enum import ProgramModes
from utils.execution_timer import timeit

VALID_FILE_EXTENSIONS: list[str] = ["jpg", "cr2", "png", "tiff", "tif"]


def are_files_equal(file1_path: str, file2_path: str) -> bool:
    return filecmp.cmp(file1_path, file2_path)


def delete_empty_subdirectories(path: str) -> None:
    walk = list(os.walk(path))
    for dir_path, _, _ in walk[::-1]:
        if len(os.listdir(dir_path)) == 0:
            os.rmdir(dir_path)


def get_file_extension(file_name: str) -> str:
    return file_name.split(".")[1].lower()


def get_file(path: str) -> dict[str, str]:
    files: dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if "duplicates" not in dirpath:
                files[file] = dirpath
    return files


@timeit(str(ProgramModes.COMPARE_DIRS))
def compare(files_1: dict[str, str], files_2: dict[str, str]) -> None:
    counter: int = 0
    for file in files_1.keys():
        if file not in files_2.keys() and get_file_extension(file) in VALID_FILE_EXTENSIONS:
            # print(f"File {file} : {files_1[file]} not in dir2")
            counter += 1
    print(f"Found {counter} files not in other dir")


@timeit(str(ProgramModes.MOVE_DUPLICATES))
def move_duplicates(dir_1_path: str, files_1: dict[str, str], files_2: dict[str, str]) -> None:
    for file in files_1.keys():
        if file in files_2.keys():
            file_path: str = os.path.join(files_1[file], file)
            file_relative_path: str = os.path.relpath(file_path, dir_1_path)
            duplicate_file_path: str = os.path.join(dir_1_path, "duplicates", file_relative_path)
            duplicates_folder: str = os.path.dirname(duplicate_file_path)

            if not os.path.exists(duplicates_folder):
                os.makedirs(duplicates_folder)
            os.rename(file_path, duplicate_file_path)
    delete_empty_subdirectories(dir_1_path)


if __name__ == "__main__":
    questions = [
        inquirer.List(
            "operation",
            message="What do you want to do?",
            choices=[ProgramModes.COMPARE_DIRS, ProgramModes.MOVE_DUPLICATES],
        )
    ]
    mode: dict[str, int] = inquirer.prompt(questions)
    if mode["operation"] == ProgramModes.COMPARE_DIRS.value:
        path1 = input("Dir 1 path: ")
        path2 = input("Dir 2 path: ")

        dir1_files: dict[str, str] = get_file(path1)
        dir2_files: dict[str, str] = get_file(path2)

        compare(dir2_files, dir1_files)

    if mode["operation"] == ProgramModes.MOVE_DUPLICATES.value:
        path1 = input("Dir to remove duplicates: ")
        path2 = input("Dir to compare: ")

        path1 = path1 if path1 != "" else r"C:\Users\janek\Dev\photo_organiser\test\test_files2\dir2"
        path2 = path2 if path2 != "" else r"C:\Users\janek\Dev\photo_organiser\test\test_files2\dir1"

        dir1_files: dict[str, str] = get_file(path1)
        dir2_files: dict[str, str] = get_file(path2)

        move_duplicates(path1, dir1_files, dir2_files)
