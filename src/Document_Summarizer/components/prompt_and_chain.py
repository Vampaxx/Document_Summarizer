from Document_Summarizer import logger 
from Document_Summarizer.utils.common import format_docs
from Document_Summarizer.components.model import ModelSetup
from Document_Summarizer.components.data_processing import UploadFileProcessing
from Document_Summarizer.config.configuration import ConfigurationManager
from Document_Summarizer.entity.config_entity import ModelConfig,UploadFileConfig

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser




class PromptAndChain(ModelSetup):

    def __init__(self,model_config          : ModelConfig,):
                        #upload_file_config  : UploadFileConfig):
        
        super().__init__(model_config)
        #self.upload_file_processor      = UploadFileProcessing(upload_config=upload_file_config)
        self.llm                        = self.model_setup()
        self.parser                     = StrOutputParser()

    def prompt_and_chain(self): 

        logger.info(f"Prompting and chain has started")

        summarizer_prompt = """
        You are an expert summarizer. Your task is twofold:
            1. Provide a concise summary of the following text, 
            2. Highlight the key points from the text by surrounding them with double asterisks (**).

        Text:
        {document_text}
        Summary: ensuring the summary is no longer than 500.
        """
        example_prompt  = PromptTemplate(
            input_variables = ["document_text"],
            template        = summarizer_prompt)

        chain = (
            {
                "document_text" : RunnablePassthrough() | format_docs
            }
            | example_prompt 
            | self.llm
            | self.parser
        )
        return chain 
                         



if __name__ == "__main__":
    manager             = ConfigurationManager()
    model_config        = manager.get_model_config()
    prompt_and_chain    = PromptAndChain(model_config=model_config)
    chain               = prompt_and_chain.prompt_and_chain()
    

