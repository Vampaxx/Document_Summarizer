import os
from dotenv import load_dotenv
from Document_Summarizer import logger
from Document_Summarizer.constants import *
from Document_Summarizer.utils.common import *
from Document_Summarizer.entity.config_entity import (ModelConfig,
                                                      UploadFileConfig)




class ConfigurationManager:
    def __init__(self,
                 config_filepath    = CONFIG_FILE_PATH,
                 params_filepath    = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)


    def get_model_config(self) -> ModelConfig:
        params  = self.params
        logger.info("Model config initialized")
        load_dotenv()
        model_config = ModelConfig(Model_name   = params.MODEL_NAME,
                                   temperature  = params.TEMPERATURE,
                                   api_key      = os.getenv("GROQ_API_KEY"))

        return model_config
    

    def get_upload_config(self) -> UploadFileConfig:

        config          = self.config.upload_files 
        logger.info("Upload file config initialized") 
        upload_config   = UploadFileConfig(docs_file_path   = config.docs_file_path,
                                           pdf_file_path    = config.pdf_file_path,
                                           text_file_path   = config.text_file_path)
        return upload_config


