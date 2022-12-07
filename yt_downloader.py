from pytube import Playlist, YouTube
import os

# Download funcs
def downl_youtube(vid):
    print("Now downloading ---->  ", vid.title)
    vid.streams.get_highest_resolution().download(output_path = get_path())
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