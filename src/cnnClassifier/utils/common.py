import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If YAML file is empty.

    Returns:
        ConfigBox: A ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
       


@ensure_annotations
def create_directories(path_to_directories: list, ignore_log: bool = True):
    """Create a list of directories.
    
    Args:
        path_to_directories (list): List of paths of directories.
        ignore_log (bool, optional): Ignore if multiple directories are to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if not ignore_log:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save JSON data.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file data.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)

def decodeImage(imgstring, fileName):
    """Decode base64 encoded image string and save it to a file.

    Args:
        imgstring (str): Base64 encoded image string.
        fileName (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    """Encode an image file into base64 format.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        str: Base64 encoded image data.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())