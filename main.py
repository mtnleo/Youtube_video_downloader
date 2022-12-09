import yt_downloader as dwn

if __name__ == "__main__":
    print("| 1 | Download a video")
    print("| 2 | Download a playlist")
    print("| 3 | Choose download path")
    opt = int(input("Choose an option: "))
    url = ""

    if opt == 1:
        url = input("Paste the URL of your video: ")
        dwn.download_vid(url)
    elif opt == 2:
        url = input("Paste the URL of your playlist: ")
        dwn.download_plist(url)
    elif opt == 3:
        path = input("Paste here your chosen download path: ")
        dwn.set_default_path(path)
        print("Current path is ->  ", dwn.get_path())
    elif opt == 4:
        url = input("Paste the URL of your playlist: ")
        vid = dwn.YouTube(url)
        dwn.download_dash_streams(vid)
    elif opt == 5:
        path = input("PASTE PATH HERE: ")
        dwn.fld.create_converter_folder(path)

    else:
        print("Invalid option.")