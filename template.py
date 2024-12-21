
import os
from pathlib import Path

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    
)

def create_file_structure(file_paths):
    """
    Creates directories and files as specified in the provided file paths.

    Args:
        file_paths (list): List of file paths to create.
    """
    for file_path in file_paths:
        path = Path(file_path)
        directory, file_name = os.path.split(path)

        # Create the directory if it does not  exist
        if directory:
            os.makedirs(directory, exist_ok=True)
            logging.info(f"Directory created: {directory} for file {file_name}")

        # Create the file if it does not exist or is empty
        if not path.exists() or path.stat().st_size == 0:
            path.touch()  ## Create an empty file
            logging.info(f"Empty file created: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")

if __name__ == "__main__":
    # Project configuration
    PROJECT_NAME = "DSProject"

    # List of files to create
    files_to_create = [
        f"src/{PROJECT_NAME}/__init__.py",
        f"src/{PROJECT_NAME}/components/__init__.py",
        f"src/{PROJECT_NAME}/components/data_ingestion.py",
        f"src/{PROJECT_NAME}/components/data_transformation.py",
        f"src/{PROJECT_NAME}/components/model_trainer.py",
        f"src/{PROJECT_NAME}/components/model_monitoring.py",
        f"src/{PROJECT_NAME}/pipelines/__init__.py",
        f"src/{PROJECT_NAME}/pipelines/training_pipeline.py",
        f"src/{PROJECT_NAME}/pipelines/prediction_pipeline.py",
        f"src/{PROJECT_NAME}/exception.py",
        f"src/{PROJECT_NAME}/logger.py",
        f"src/{PROJECT_NAME}/utils.py",
        "main.py",
        "app.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
    ]

    # Create the file structure/call the funcation
    create_file_structure(files_to_create)
