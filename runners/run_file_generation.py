import json

import yaml

from data_types.file_generation import FileGenerationParams
from file_generator.random_file_generator import generate_files


def run_random_file_generation() -> None:
    with open("params/files_to_generate.yaml", "r", encoding="UTF-8") as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)
        json_params = json.dumps(yaml_object)
        file_generation_params = FileGenerationParams.model_validate_json(json_params)

    generate_files(output_dir_rel_path=file_generation_params.output_dir, files=file_generation_params.files)
