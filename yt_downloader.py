from pytube import Playlist, YouTube

save_path = "D:\Video Downloads"

def downl_youtube(vid):
    print("Now downloading ---->  ", vid.title)
    vid.streams.get_highest_resolution().download(output_path = save_path)

def download_vid(url):
    vid = YouTube(url)
    downl_youtube(vid)

def download_plist(url):
    plist = Playlist(url)
    for vid in plist:
        downl_youtube(vid)
