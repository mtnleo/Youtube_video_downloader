from pytube import Playlist, YouTube, Channel
import folder_handling as fld
import os

# Download funcs
def get_artist_path(name):
    path = get_path()
    artist_folder = fld.create_folder_name(name)
    new_path = fld.create_new_dir_path(path, artist_folder)

    if fld.check_folder_exists(new_path) == False:
        fld.create_folder_dir(new_path)
        
    return new_path

def downl_youtube(vid):
    print("Now downloading ---->  ", vid.title)
    channel = Channel(vid.channel_url)
    vid.streams.get_highest_resolution().download(output_path = get_artist_path(channel.channel_name))
    print("Done ---->  ", vid.title)

def download_vid(url):
    vid = YouTube(url)
    downl_youtube(vid)

def download_plist(url):
    plist = Playlist(url)
    for vid in plist:
        downl_youtube(vid)

# PATH funcs
def set_default_path(pathName):
    if os.path.exists(pathName) == False:
        pathName = os.getcwd()
        print(f"Path not found, setting {pathName} as default path.")

    with open("path.txt", "w") as file:
        file.write(pathName)

def get_path():
    path = ""
    try:
        with open("path.txt", "r") as file:
            path = file.readline()
    except:
        path = os.getcwd()

    return path