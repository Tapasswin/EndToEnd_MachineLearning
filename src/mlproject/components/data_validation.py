# components update

import os
from mlproject import logger
from mlproject.entity.config_entity import *
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            status = []
            
            for col in all_cols:
                if col not in all_schema:
                    status.append(False)
                elif data[col].dtype != self.config.all_schema[col]:
                    status.append(False)
                else:
                   status.append(True)
                   
            if False in status:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status1: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")


            return validation_status
        
        except Exception as e:
            raise e