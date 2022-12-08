from pytube import Playlist, YouTube, Channel
import folder_handling as fld
import os
import subprocess

# Download funcs
# Dash streams
def get_dash_streams(vid):
    adaptiveVid = list(vid.streams.filter(adaptive=True, type="video"))
    adaptiveAud = list(vid.streams.filter(adaptive=True, type="audio"))

    return adaptiveVid[0], adaptiveAud[-1]

def download_dash_streams(vid):
    dash_vid, dash_aud = get_dash_streams(vid)
    channel = Channel(vid.channel_url)

    artist_path = get_artist_path(channel.channel_name)

    conv_path = get_path()
    conv_path = fld.get_converter_folder(conv_path)

    dash_vid.download(output_path = conv_path)
    dash_aud.download(output_path = conv_path)

    files_list = os.listdir(conv_path)
    new_file_name = files_list[0][:-4] + "_c.mp4"
    print("LLEGA")

    cd = f"cd {conv_path}"
    command = f"ffmpeg -i {files_list[0]} -i {files_list[1]} -c:v copy -c:a aac {new_file_name}"
    subprocess.call(cd, shell=True)
    subprocess.call(command, shell=True)


# get path
def get_artist_path(name):
    path = get_path()
    artist_folder = fld.create_folder_name(name)
    new_path = fld.create_new_dir_path(path, artist_folder)

    if fld.check_folder_exists(new_path) == False:
        fld.create_folder_dir(new_path)
        
    return new_path

# progressive video

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

# Path funcs
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

