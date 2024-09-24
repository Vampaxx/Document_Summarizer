from Document_Summarizer import logger
from Document_Summarizer.config.configuration import ConfigurationManager
from Document_Summarizer.components.prompt_and_chain import PromptAndChain


STAGE_NAME = "Prompt and chain stage"


class PromptAndChainPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            manager             = ConfigurationManager()
            model_config        = manager.get_model_config()
            prompt_and_chain    = PromptAndChain(model_config=model_config)
            chain               = prompt_and_chain.prompt_and_chain()
    
            return chain 
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"<<<____stage____{STAGE_NAME}_____started >>>")
        obj     = PromptAndChainPipeline()
        chain    = obj.main()
        logger.info(f"<<<____stage____{STAGE_NAME}____completed \n\n===========================================>>>")

    except Exception as e:
        raise e