import os

create_folder_name = lambda name: name.replace(" ", "_")

create_new_dir_path = lambda path, folder: path + f"\{folder}"

check_folder_exists = lambda path: os.path.exists(path)

check_converter_exists = lambda path: os.path.isdir(path)

def create_folder_dir(path):
    os.mkdir(path)

def get_converter_folder(path):
    new_path = f"{path}\\converter"
    if check_converter_exists(new_path) == False:
        os.mkdir(new_path)

    return new_path