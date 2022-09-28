from pytube import YouTube
# import module.view as view
from glob import glob
from shutil import move
from os import mkdir


def connection(link, tr):
    yt = ""
    try:
        yt = YouTube(link)
    except:
        print("connection error" + "\n" + "try in {} time".format(tr))
        if tr > 0:
            connection(link, (tr - 1)) 
        else:
            print("Failed")
            return -1
    return yt


def get_info(yt):
    data = dict()
    data['video 1'] = dict()

    data['video 1']['title'] = yt.title
    data['video 1']['length'] = "{:02d}:{:02d}".format((yt.length // 60), (yt.length % 60))
    data['video 1']['author'] = yt.author
    
    return data


def resolution(yt):
    result = list()

    for res in yt.streams.filter(progressive=True):
        result.append(res.resolution)

    # return view.resolution(result, 'single')


def download(yt, res="720p"):

    ys = yt.streams.get_by_resolution(res)
    
    if get_video(ys, yt.title, 3):
        change_folder()


def get_video(ys, name, live):
    try:
        ys.download()
        return True
    except:
        if live > 0:
            
            get_video(ys, name, (live - 1))
        else:
            
            return False


def change_folder():
    file = glob("*.mp4")

    if len(file) == 0:
        file = glob("*.mkv")

    file = file[0]

    try:
        move(file, "Downloaded/" + file)
    except FileNotFoundError:
        mkdir("Downloaded")
        move(file, "Downloaded/" + file)
    finally :
        print("YOOOOOOOOOOOOOOOOOOOOOOOOO")
