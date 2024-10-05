import json
import os

import yaml
from data_types.file_generation import FileGenerationParams

from src.utils.load_yaml import parse_from_yaml


class FileGenerator:
    def __init__(self) -> None:
        self.params = parse_from_yaml(path_to_yaml=os.path.join(os.path.dirname(__file__), "files_to_generate.yaml"))

    @staticmethod
    def get_output_dir_full_path(output_dir_rel_path: str) -> str:
        current_path: str = os.getcwd()
        generated_files_path: str = os.path.join(current_path, "file_generator", output_dir_rel_path)
        return generated_files_path

    @staticmethod
    def assert_generated_files_path_exist(path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    def generate_files(self, output_dir_rel_path: str, files: list[FileGenerationParams]) -> None:
        output_dir_path: str = self.get_output_dir_full_path(output_dir_rel_path)
        self.assert_generated_files_path_exist(output_dir_path)
        for file in files:
            assert isinstance(file.name, str)
            assert isinstance(file.size, int)

            new_file_path: str = os.path.join(output_dir_path, file.name)
            with open(new_file_path, "wb") as fout:
                fout.write(os.urandom(file.size * KILOBYTE))

    def run_random_file_generation(self) -> None:
        with open("params/files_to_generate.yaml", "r", encoding="UTF-8") as yaml_in:
            yaml_object = yaml.safe_load(yaml_in)
            json_params = json.dumps(yaml_object)
            file_generation_params = FileGenerationParams.model_validate_json(json_params)
        self.generate_files(output_dir_rel_path=file_generation_params.output_dir, files=file_generation_params.files)
