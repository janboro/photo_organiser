from pydantic import BaseModel


class FileToGenerate(BaseModel):
    name: str
    size: int  # in kilobytes


class FileGenerationParams(BaseModel):
    output_dir: str
    files: list[FileToGenerate]
