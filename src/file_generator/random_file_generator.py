import json
import os

from file_generator.data_types.file_generation import FileGenerationParams, FileToGenerate
from utils.load_yaml import parse_from_yaml


class FileGenerator:
    ROOT_DIR: str = os.getcwd()
    CURRENT_DIR: str = os.path.dirname(__file__)

    def __init__(self) -> None:
        self.params = parse_from_yaml(path_to_yaml=os.path.join(self.CURRENT_DIR, "files_to_generate.yaml"))

    def get_output_dir_full_path(self, output_dir_rel_path: str) -> str:
        generated_files_path: str = os.path.join(self.ROOT_DIR, output_dir_rel_path)
        return generated_files_path

    @staticmethod
    def assert_generated_files_path_exist(path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    def generate_files(self, output_dir_rel_path: str, files: list[FileToGenerate]) -> None:
        output_dir_path: str = self.get_output_dir_full_path(output_dir_rel_path)
        self.assert_generated_files_path_exist(output_dir_path)
        for file in files:
            with open(os.path.join(output_dir_path, file.name), "wb") as fout:
                fout.write(os.urandom(file.size * self.params["kilobyte"]))

    def run_random_file_generation(self) -> None:
        json_params: str = json.dumps(self.params["generate_files"])
        file_generation_params: FileGenerationParams = FileGenerationParams.model_validate_json(json_params)
        self.generate_files(output_dir_rel_path=file_generation_params.output_dir, files=file_generation_params.files)
