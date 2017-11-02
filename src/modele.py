from threading import Thread
youtube_dl=__import__("youtube_dl")
############################################################

options = {
    'format': 'best',
    'extractaudio': False,  # only keep the audio
    'audioformat': 'mp3',  # convert to mp3
    'noplaylist': True,  # only download single song, not playlist
    'quiet': False,
    'no_warnings': True,
    'ignoreerrors': True,
    'writethumbnail': True,  #
    'playliststart': 0,  #
    'playlistend': 0,
    'writeautomaticsub': False,
    'proxy': ''
}

save_directory = ''
curent_file_metadata = {}
th = None


############################################################

############################################################

def extracteMetaData(url):
    global curent_file_metadata, options
    ydl = youtube_dl.YoutubeDL(options)
    with ydl:
        curent_file_metadata = ydl.extract_info(url, download=False)

    return curent_file_metadata


############################################################

def download(url):
    global options, curent_file_metadata, save_directory, final_file_name
    # extracteMetaData(url)
    final_file_name = curent_file_metadata['title'] + '.' + curent_file_metadata['ext']
    options['outtmpl'] = save_directory + "/" + final_file_name
    options['writesubtitles'] = curent_file_metadata['title'] + '.stl',

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])


def init_download(url):
    global th
    th = Thread(target=download, args=(url,))
    th.start()


def stop_download():
    global th
    if th != None and th.isAlive():
        th = None

###########################################################################################"


