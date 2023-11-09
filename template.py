import os
from pathlib import Path

############################## Directory #############################
dir_list = [
    "src",
    "notebooks"
]

for dir_ in dir_list:
    os.makedirs(dir_,exist_ok=True)


############################### Files ##################################
files = [
    Path("src","__init__.py"),
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    "requirements.txt",
    "README.md"
]

for file_ in files:
    with open(file_, "w") as f:
        pass