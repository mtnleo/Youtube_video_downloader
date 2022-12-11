import yt_downloader as dwn

# keep the program running
cont = 'y'

# so it will come here again, after changing directory to the artist's folder
CWD = dwn.os.getcwd()

if __name__ == "__main__":
    while cont == 'y':
        print("| 1 | Download a video")
        print("| 2 | Download a playlist")
        print("| 3 | Choose download path")
        opt = int(input("Choose an option: "))
        url = ""

        if opt == 1:
            url = input("Paste the URL of your video: ")
            dwn.download_vid(url, CWD)
        elif opt == 2:
            url = input("Paste the URL of your playlist: ")
            dwn.download_plist(url, CWD)
        elif opt == 3:
            path = input("Paste here your chosen download path: ")
            dwn.set_default_path(path)
            print("Current path is ->  ", dwn.get_path(CWD))

        else:
            print("Invalid option.")

        cont = input("> Do you want to continue downloading videos? ('y/n')\n")