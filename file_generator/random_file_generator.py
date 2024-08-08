import os

from data_types.file_generation import FileGenerationParams

KILOBYTE: int = 2**10


def get_output_dir_full_path(output_dir_rel_path: str) -> str:
    current_path: str = os.getcwd()
    generated_files_path: str = os.path.join(current_path, "file_generator", output_dir_rel_path)
    return generated_files_path


def assert_generated_files_path_exist(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def generate_files(output_dir_rel_path: str, files: list[FileGenerationParams]) -> None:
    output_dir_path: str = get_output_dir_full_path(output_dir_rel_path)
    assert_generated_files_path_exist(output_dir_path)
    for file in files:
        assert isinstance(file.name, str)
        assert isinstance(file.size, int)

        new_file_path: str = os.path.join(output_dir_path, file.name)
        with open(new_file_path, "wb") as fout:
            fout.write(os.urandom(file.size * KILOBYTE))
