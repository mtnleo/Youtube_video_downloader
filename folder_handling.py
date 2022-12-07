import os

create_folder_name = lambda name: name.replace(" ", "_")

create_new_dir_path = lambda path, folder: path + f"\{folder}"

check_folder_exists = lambda path: os.path.exists(path)

def create_folder_dir(path):
    os.mkdir(path)

