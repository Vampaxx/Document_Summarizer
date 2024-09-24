from Document_Summarizer import logger
from Document_Summarizer.config.configuration import ConfigurationManager
from Document_Summarizer.components.data_processing import UploadFileProcessing


STAGE_NAME = "Upload file processing stage"


class UploadFileProcessingPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            manager                 = ConfigurationManager()
            upload_file_config      = manager.get_upload_config()
            upload_file_processing  = UploadFileProcessing(upload_config=upload_file_config)
            
            return upload_file_processing,upload_file_config
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"<<<____stage____{STAGE_NAME}_____started >>>")
        obj     = UploadFileProcessingPipeline()
        file     = obj.main()
        logger.info(f"<<<____stage____{STAGE_NAME}____completed \n\n===========================================>>>")

    except Exception as e:
        raise e