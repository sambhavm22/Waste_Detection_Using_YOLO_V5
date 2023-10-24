from sympy import true
import yaml
import os.path
import sys
import base64
from ensure import ensure_annotations

from WasteDetection.exception import AppException
from WasteDetection.logger import logging

@ensure_annotations
def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e

@ensure_annotations
def write_yaml_file(file_path: str, content: object, replace: bool) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")  
    except Exception as e:
        raise AppException(e, sys)
    

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+fileName,'wb') as f:
        f.write(imgdata)
        f.close()  

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())        