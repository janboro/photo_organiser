import os
from dataclasses import dataclass, field

from utils.file_content_hash import get_file_content_hash


@dataclass
class File:
    path: str
    name: str = field(init=False)
    content_hash: str = field(init=False)

    def __post_init__(self) -> None:
        self.name = os.path.basename(self.path)
        self.content_hash = get_file_content_hash(self.path)
