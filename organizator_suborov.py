import os
from pathlib import Path

ext_num = []

dir_str = input("Paste a dircetory from your PC: ")
dir_path = Path(dir_str)

if dir_path.is_dir() and os.path.exists(dir_path):
    files = os.listdir(dir_path)
    print(files)

for file in files:
    name, ext = os.path.splitext(file)
    if ext not in ext_num:
        ext_num.append(ext)

print(ext_num)
