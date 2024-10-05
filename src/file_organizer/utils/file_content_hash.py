import hashlib
import os

import yaml

# TODO Use os path and join
with open("params/file_read_params.yaml", "r", encoding="UTF-8") as params:
    PARAMS = yaml.load(params, Loader=yaml.SafeLoader)


def get_file_content_hash(file_path: str) -> str:
    with open(file_path, "rb") as f:
        MB: int = 8 * 2**20
        if os.path.getsize(file_path) > PARAMS["MAX_MEMORY_USAGE"] * MB:
            # Hashing big files in chunks to reduce memory usage
            sha256 = hashlib.sha256()
            while True:
                data = f.read(PARAMS["BUFFER_SIZE"])
                if not data:
                    break
                sha256.update(data)
        else:
            sha256 = hashlib.sha256(f.read())
    return sha256.hexdigest()
