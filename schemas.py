from pydantic import BaseModel


class UploadData(BaseModel):
    FilePath: str
