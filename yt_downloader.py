from pytube import Playlist, YouTube, Channel
import folder_handling as fld
import os
import subprocess

# Download funcs
# Dash streams
def get_dash_streams(vid):
    adaptiveVid = list(vid.streams.filter(adaptive=True, type="video"))
    adaptiveAud = list(vid.streams.filter(adaptive=True, type="audio"))

    for vid in adaptiveVid:
        if "mp4" in str(vid):
            returnVid = vid
            break

    return returnVid, adaptiveAud[-1]

def download_dash_streams(vid, CWD):
    dash_vid, dash_aud = get_dash_streams(vid)
    channel = Channel(vid.channel_url)

    artist_path = get_artist_path(channel.channel_name, CWD)

    conv_path = get_path(CWD)
    conv_path = fld.get_converter_folder(conv_path)

    dash_vid.download(output_path = conv_path)
    dash_aud.download(output_path = conv_path)

    files_list = os.listdir(conv_path)
    no_spaces_file_list = [name.replace(" ", "_") for name in files_list]

    files_list_path = [conv_path + f"\\{name}" for name in files_list]
    no_spaces_file_list_path = [conv_path + f"\\{name}" for name in no_spaces_file_list]
    
    for name1, name2 in zip(files_list_path, no_spaces_file_list_path):
        fld.change_file_name(name1, name2)

    new_file_name = files_list[0][:-4] + "_c.mp4"
    new_file_path = os.path.join(conv_path, new_file_name)
    artist_file_path = os.path.join(artist_path, new_file_name)

    # change directory and download
    os.chdir(conv_path)
    command = ["ffmpeg", "-i", no_spaces_file_list[0], "-i", no_spaces_file_list[1], "-c:v", "copy", "-c:a", "aac", new_file_name]
    subprocess.call(command, shell=True)

    #move the new video to the artist's folder
    os.replace(new_file_path, artist_file_path)

    # Delete the conversion folder files
    fld.delete_directory_files(no_spaces_file_list_path)


# get path
def get_artist_path(name, CWD):
    path = get_path(CWD)
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

def download_vid(url, CWD):
    try:
        vid = YouTube(url)
    except:
        print("That URL doesn't exist")
        return False
    
    download_dash_streams(vid, CWD)
    os.system("cls")
    print(f"Done downloading ----->   |  {vid.title}  |")

def download_plist(url, CWD):
    try:
        plist = Playlist(url)
    except:
        print("That URL doesn't exist")
        return False
    
    for vid in plist.videos:
        download_dash_streams(vid, CWD)
        os.system("cls")
        print(f"Done downloading ----->   |  {vid.title}  |")
 
# Path funcs
def set_default_path(pathName):
    if os.path.exists(pathName) == False:
        pathName = os.getcwd()
        print(f"Path not found, setting {pathName} as default path.")

    with open("path.txt", "w") as file:
        file.write(pathName)

def get_path(cwd):
    path = ""
    os.chdir(cwd)
    try:
        with open("path.txt", "r") as file:
            path = file.readline()
    except:
        path = os.getcwd()
        

    return path

