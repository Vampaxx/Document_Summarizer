from Document_Summarizer import logger 
from Document_Summarizer.components.model import ModelSetup
from Document_Summarizer.config.configuration import ConfigurationManager
from Document_Summarizer.entity.config_entity import ModelConfig,UploadFileConfig
from Document_Summarizer.utils.common import (load__txt_file,
                                              load_docs_file,
                                              load_pdf_file)




class UploadFileProcessing:

    def __init__(self, upload_config: UploadFileConfig):
        self.upload_config  = upload_config

    def __call__(self, format: str):
        """
        Process the uploaded file based on its format (.pdf,.txt,.docs).
        """
        if format.lower() == 'pdf':
            logger.info("Processing pdf format file")
            pdf     = load_pdf_file(self.upload_config.pdf_file_path) 
            return pdf 
        elif format.lower() == "txt":
            logger.info("Processing txt foramt file") 
            txt     = load__txt_file(self.upload_config.text_file_path) 
            return txt 
        elif format.lower() in ["docx", "docs", "doc"]:
            logger.info("Processing docs foramt file") 
            docs    = load_docs_file(self.upload_config.docs_file_path) 
            return docs
        else:
            raise ValueError(f"Unsupported file format: {format}")


if __name__ == "__main__" :
    manager                 = ConfigurationManager()
    model_config            = manager.get_model_config()
    upload_file_config      = manager.get_upload_config()
    

    upload_file_processing  = UploadFileProcessing(model_config     = model_config,
                                                   upload_config    = upload_file_config)

    print(upload_file_processing.upload_data_processing())


