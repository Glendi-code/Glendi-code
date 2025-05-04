import os
from pathlib import Path

dir_str = input("Paste a dircetory from your PC: ")
if os.path.exists(dir_str):
    dir_path = Path(dir_str)
    os.listdir(dir_path)

