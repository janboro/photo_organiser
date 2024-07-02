import unittest
import os
import shutil


def get_test_dir_path() -> str:
    return os.path.join(os.getcwd(), "test", "test_files")


def create_file(file_path: str, extension: str) -> None:
    open(file_path + "." + extension, "x", encoding="UTF-8")


def create_dir_if_not_exists(path: str) -> str:
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def build_unstructured_test_files() -> None:
    dir_1_test_path: str = create_dir_if_not_exists(os.path.join(get_test_dir_path(), "dir1"))
    for extension in ["CR2", "jpg"]:
        for i in range(5):
            create_file(os.path.join(dir_1_test_path, f"00{i}_IMG"), extension)


def build_structured_test_files() -> None:
    dir_2_test_path: str = create_dir_if_not_exists(os.path.join(get_test_dir_path(), "dir2"))

    day_1_dir: str = create_dir_if_not_exists(os.path.join(dir_2_test_path, "day_1"))
    day_2_dir: str = create_dir_if_not_exists(os.path.join(dir_2_test_path, "day_2"))
    edit_dir: str = create_dir_if_not_exists(os.path.join(dir_2_test_path, "edit"))
    selected_dir: str = create_dir_if_not_exists(os.path.join(dir_2_test_path, "edit", "selected"))
    for i in range(3):
        create_file(os.path.join(day_1_dir, f"00{i}_IMG"), "CR2")
    for i in range(3, 5):
        create_file(os.path.join(day_2_dir, f"00{i}_IMG"), "CR2")
    for i in range(5):
        create_file(os.path.join(edit_dir, f"00{i}_IMG"), "jpg")
    for i in range(5):
        create_file(os.path.join(selected_dir, f"00{i}_IMG"), "tiff")


def create_test_dirs() -> None:
    build_unstructured_test_files()
    build_structured_test_files()


def tear_down_test_dirs() -> None:
    shutil.rmtree(get_test_dir_path())


class TestFileOrganiser(unittest.TestCase):
    def test_compare(self) -> None:
        pass

    def test_all(self) -> None:
        self.test_compare()


if __name__ == "__main__":
    # TestFileOrganiser().test_all()
    tear_down_test_dirs()
    create_test_dirs()
    tear_down_test_dirs()