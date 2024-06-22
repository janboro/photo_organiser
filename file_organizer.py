import os

VALID_FILE_EXTENSIONS: list[str] = ["jpg", "cr2", "png", "tiff", "tif"]


def get_file_extension(file_name: str) -> str:
    return file_name.split(".")[1].lower()


def get_file(path: str) -> dict[str, str]:
    files: dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            files[file] = dirpath
    return files


def compare(files_1: dict[str, str], files_2: dict[str, str]) -> None:
    for file in files_1.keys():
        if file not in files_2.keys() and get_file_extension(file) in VALID_FILE_EXTENSIONS:
            print(f"File {file} : {files_1[file]} not in dir2")


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


if __name__ == "__main__":
    mode: str = input("What do you want to do? (move|compare|move_duplicates)")

    if mode == "compare":
        path1 = input("Dir 1 path: ")
        path2 = input("Dir 2 path: ")

        dir1_files: dict[str, str] = get_file(path1)
        dir2_files: dict[str, str] = get_file(path2)

        compare(dir2_files, dir1_files)

    if mode == "move_duplicates":
        path1 = input("Dir to remove duplicates: ")
        path2 = input("Dir to compare: ")

        path1 = path1 if path1 != "" else r"C:\Users\janek\Dev\photo_organiser\test\test_files2\dir1"
        path2 = path2 if path2 != "" else r"C:\Users\janek\Dev\photo_organiser\test\test_files2\dir2"

        dir1_files: dict[str, str] = get_file(path1)
        dir2_files: dict[str, str] = get_file(path2)
        move_duplicates(path1, dir1_files, dir2_files)
