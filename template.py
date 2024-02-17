import os
from pathlib import Path 
import logging

#Logging string
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name='cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Creating the file and folder structrs
# for every path we need to create folder and file seperately with logging info, if file is not already created process for new one
# _else  not

for filepath in list_of_files:
    # Convert filepath to a Path object
    filepath = Path(filepath)
    
    # Split filepath into directory and filename
    filedir, filename = os.path.split(filepath)

    # Check if directory is not empty (non-empty string)
    if filedir != "":
        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file:{filename}")

    # Check if file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass  # Do nothing, just create an empty file
        logging.info(f"Create empty file:{filepath}")

    else:
        logging.info(f"{filename} already exists")

