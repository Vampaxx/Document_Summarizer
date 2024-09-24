import os 
import yaml
import json

from box import ConfigBox
from typing import Any
from pathlib import Path

from ensure import ensure_annotations
from box.exceptions import BoxValueError

from Document_Summarizer import logger
from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader,TextLoader


@ensure_annotations
def load_docs_file(file_path: str):
    try:
        new_file_path   = file_path.replace(" ","_").replace("-","_")
        logger.info("file name is replaced") 
        os.rename(file_path,new_file_path) 
        logger.info("Rename the file")
        logger.info("Loading docs file ====>>>>")
        docs            = Docx2txtLoader(Path(new_file_path)).load_and_split() 
        logger.info("Loading completed <<<<====")
        return docs  
    except Exception as e:
        raise e 

@ensure_annotations
def load_pdf_file(file_path: str):
    try: 
        new_file_path   = file_path.replace(" ","_").replace("-","_")
        os.rename(file_path,new_file_path) 
        logger.info("Rename the file")
        logger.info("Loading pdf file ====>>>>")
        pdf = PyPDFLoader(Path(file_path)).load_and_split()
        logger.info("Loading completed <<<<====")
        return pdf 
    except Exception as e:
        raise e 
    

@ensure_annotations
def load__txt_file(file_path:str):
    try:
        new_file_path   = file_path.replace(" ","_").replace("-","_")
        os.rename(file_path,new_file_path) 
        logger.info("Rename the file")
        logger.info("Loading text file====>>>>")
        text            = TextLoader(Path(new_file_path)).load_and_split()
        logger.info("Loading completed <<<<====")
        return text 
    except Exception as e:
        raise e 



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)


@ensure_annotations
def allowed_file(filename):
    ALLOWED_EXTENSIONS          = {'pdf', 'txt', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




if __name__ == "__main__":
    
    docx_file_path  = "notebook\demo\Fittlyf_DS_Team_Assignment.docx"
    pdf_file_path   = "notebook\demo\proof_of_concept_9.pdf"
    text_file_path  = "notebook\demo\story_of_haripotter.txt"

    file = load_pdf_file(pdf_file_path)
    print(file)