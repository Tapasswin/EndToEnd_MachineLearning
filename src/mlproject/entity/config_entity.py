# After updating the Config.yaml file 
# With the below code we update it in 
# src/entity/config_entity.py

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path
