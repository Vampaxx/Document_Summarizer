from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    Model_name              : str 
    temperature             : int 
    api_key                 : Optional[str]


@dataclass(frozen=True) 
class UploadFileConfig:
    pdf_file_path       : Path
    text_file_path      : Path
    docs_file_path      : Path