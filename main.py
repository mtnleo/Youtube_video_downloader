import yt_downloader as dwn

if __name__ == "__main__":
    print("| 1 | Download a video")
    print("| 2 | Download a playlist")
    opt = int(input("Choose an option: "))
    url = ""

    if opt == 1:
        url = input("Paste the URL of your video: ")
        dwn.download_vid(url)
    elif opt == 2:
        url = input("Paste the URL of your playlist: ")
        dwn.download_plist(url)
    else:
        print("Invalid option.")