import os, shutil
from pathlib import Path

ext_num = []
new_paths = []

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

for ext in ext_num:
    new_path = dir_path.joinpath(ext[1:] if ext.startswith('.') else ext)
    new_paths.append(new_path)
    os.makedirs(new_path, exist_ok=True)

for file in files:
    src_file = Path(os.path.join(dir_path, file))
    if src_file.is_file():
        name, ext = os.path.splitext(file)
        dest_folder = new_paths[ext_num.index(ext)]
        shutil.move(str(src_file), str(dest_folder))



