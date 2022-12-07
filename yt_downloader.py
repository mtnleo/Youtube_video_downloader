from pytube import Playlist

save_path = "D:\Video Downloads"

p_list = Playlist("https://www.youtube.com/watch?v=oozQ4yV__Vw&list=PL68y5Mx2RoPjW8t7PznHLNjXFDOSOMlme")

for vid in p_list.videos:
    print("Now downloading ---->  ", vid.title)
    vid.streams.get_highest_resolution().download(output_path = save_path)

