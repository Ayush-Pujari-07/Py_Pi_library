import os
import logging

from pathlib import Path

# Create terminal logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

# Provide project Name
while True:
    project_name = input("Enter your project name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# List of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exceptions.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_project.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Directory created: {file_dir}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"File created: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")

