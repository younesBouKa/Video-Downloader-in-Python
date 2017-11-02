import tkinter as tk
import tkinter.filedialog as tfd
from tkinter import filedialog as fd
from tkinter import ttk
from threading import Thread
from os.path import expanduser
import modele as code
import time 

import urllib as urllib
###############################################################
# in this file i make a simple GUI 
############################################################
#main window
root=tk.Tk()
root.geometry('800x450+400+400')
root.title("Youtube-DL Downloader")
root.configure(background='White')

# video informations
curent_file_url=""
filename_label_var=tk.StringVar()
filesize_label_var=tk.StringVar()
file_thumbnail_var=tk.StringVar()
location_textarea_var =tk.StringVar()
url_textarea_var =tk.StringVar()
save_directory = expanduser("~")

video_or_playlist_var=tk.StringVar()
audio_var = tk.StringVar()
subtitles_var=tk.StringVar()

# on downloading variables
speed_label_var=tk.StringVar()
percent_label_var=tk.StringVar()
NOF_label_var=tk.StringVar()
status_label_var=tk.StringVar()
downloaded_label_var=tk.StringVar()
remaining_time_var=tk.StringVar()
max_progress=100


#########################################################""
init_info_frame=tk.Frame(root,bg='',width=720,height=80)
init_info_frame.place(x=50,y=40)

# file url label
url_label=tk.Label(init_info_frame,text='URL',
                   bg='white',
                   fg='black'
                   )
url_label.place(x=0,y=0,width=100,height=30)


#url textarae
url_textarea=tk.Entry(init_info_frame,
                      textvariable=url_textarea_var,
                      bg='white',
                      fg='blue'
                      )
url_textarea.focus_set()
url_textarea.place(x=100,y=0,width=500,height=30)

# paste button
def paste():
    global curent_file_url,url_textarea_var,filename_label_var,save_directory,video_or_playlist_var,root
    clip=root.clipboard_get()
    if len(clip)<10:
        return ""
    curent_file_url=clip
    url_textarea_var.set(curent_file_url)
    code.extracteMetaData(curent_file_url)
    if code.curent_file_metadata is None:
        return ""
    """
    for key,value in code.curent_file_metadata.items():
        print("{} == {}".format(key,value))
    """
    filename_label_var.set(code.curent_file_metadata['title'])
    if code.curent_file_metadata['playlist'] is None:
        video_or_playlist_var.set('video')
    else:
        video_or_playlist_var.set('playlist')
    code.save_directory=save_directory
    download_button.configure(state='normal')

paste_button=tk.Button(init_info_frame,
                      text='Paste URL',
                      command=paste,
                      bg='white',
                      fg='blue'
                      )
paste_button.place(x=620,y=0,width=100,height=30)


# location label
location_label=tk.Label(init_info_frame,
                        text='Save In',
                        bg='white',
                        fg='black'
                        )
location_label.place(x=0,y=40,width=100,height=30)


# location textarea
location_textarea_var.set(save_directory)
location_textarea=tk.Entry(init_info_frame,
                           textvariable=location_textarea_var,
                           bg='white',
                           fg='blue'
                           )
#location_textarea.focus_set()
location_textarea.place(x=100,y=40,width=500,height=30)


# find location
def select_location():
    global save_directory,location_textarea_var
    #folder=tk.tkFileDialog.askdirectory(initialdir='/home') # python 2
    #folder = fd.askdirectory(initialdir='/home') # python 3
    #folder=tfd.askdirectory(initialdir=save_directory,title="Save in")
    #if len(folder)!=0:
        #save_directory=folder
    location_textarea_var.set(save_directory)

find_button=tk.Button(init_info_frame,
                      text='Save In',
                      command=select_location,
                      bg='white',
                      fg='blue'
                      )
find_button.place(x=620,y=40,width=100,height=30)

########################################################################
advanced_info_frame=tk.Frame(root,bg='',width=720,height=120)
advanced_info_frame.place(x=50,y=120)


# just video
video_or_playlist_var.set('')
just_video = ttk.Radiobutton(
                             advanced_info_frame,
                             text="Video",
                             variable=video_or_playlist_var,
                             value="video",
                             command=None,
                             
        ).place(
          x=110,
          y=5,
          width=100,
          height=30
        )
# playlist
playlist = ttk.Radiobutton(
                             advanced_info_frame,
                             text="Palylist",
                             variable=video_or_playlist_var,
                             value="playlist",
                             command=None
        ).place(
          x=230,
          y=5,
          width=100,
          height=30
        )
# Audio 
audio_var.set('no')
audio=ttk.Checkbutton(
					 advanced_info_frame,
					 text="Audio Extract",
					 variable=audio_var,
					 command=None,
					 onvalue='yes',
					 offvalue='no'
        ).place(
          x=350,
          y=5,
          width=100,
          height=30
          )
          
# from to

# subtitles
subtitles_var.set('no')
subtitles=ttk.Checkbutton(
					 advanced_info_frame,
					 text="Subtitles",
					 variable=subtitles_var,
					 command=None,
					 onvalue='yes',
					 offvalue='no'
        ).place(
          x=470,
          y=5,
          width=100,
          height=30
          )
 
# format


# file name label
tk.Label(advanced_info_frame,
         text='Video Name',
         bg='white',
         fg='black'
         ).place(x=15,
                 y=80,
                 width=90,
                 height=30)

# file name 
tk.Label(advanced_info_frame,
                        textvariable=filename_label_var,
                        bg='#ADD8E6',
                        fg='black'
                        ).place(
                                x=105,
                                y=80,
                                width=500,
                                height=30
                                )

# thumbnail of video
'''
path='No_file.jpg'

if 'title' in code.curent_file_metadata:
	path=save_directory+"/"+code.curent_file_metadata['title']+'.jpg'
	urllib.urlretrieve(code.curent_file_metadata['thumbnail'], path)
	img = ImageTk.PhotoImage(Image.open(path))	
	thumbnail = tk.Label(advanced_info_frame, image = img)
	thumbnail.place(x=600,y=0,width=100,height=100)
'''

#######################################################################
download_frame=tk.Frame(root,bg='',width=720,height=120)
download_frame.place(x=50,y=240)

# file size 
tk.Label(download_frame,
         text='File Size :',
         bg='white',
         fg='black',
         ).place(
         x=50,
         y=5,
         width=100,
         height=30
         )
         
filesize_label_var.set("0 Mb")
filesize_label=tk.Label(download_frame,
                        textvariable=filesize_label_var,
                        bg='#ADD8E6',
                        fg='black'
                        )
filesize_label.place(x=160,y=5,width=100,height=30)

# downloaded size
tk.Label(download_frame,
         text='Downloaded :',
         bg='white',
         fg='black',
         ).place(
         x=50,
         y=40,
         width=100,
         height=30
         )
downloaded_label_var.set("0 Mb")
downloaded_label=tk.Label( download_frame,
                        textvariable=downloaded_label_var,
                        bg='#ADD8E6',
                        fg='black'
                        )
downloaded_label.place(x=160,y=40,width=100,height=30)


# download speed
tk.Label(download_frame,
         text='Speed :',
         bg='white',
         fg='black',
         justify='left'
         ).place(
         x=440,
         y=5,
         width=120,
         height=30
         )

speed_label_var.set("0 Kb/S")
speed_label=tk.Label(   download_frame,
                        textvariable=speed_label_var,
                        bg='#ADD8E6',
                        fg='black'
                        )
speed_label.place(x=565,y=5,width=100,height=30)

# remaining time
tk.Label(download_frame,
         text='Remaining Time :',
         bg='white',
         fg='black',
         justify='left'
         ).place(
         x=440,
         y=40,
         width=120,
         height=30
         )

remaining_time_var.set("1 S")
remaining_time_label=tk.Label(   download_frame,
                        textvariable=remaining_time_var,
                        bg='#ADD8E6',
                        fg='black',
                        justify='center'
                        )
remaining_time_label.place(x=565,y=40,width=100,height=30)


status_label_var.set("")
status_label=tk.Label(   download_frame,
                        textvariable=status_label_var,
                        bg='white',
                        fg='black',
                        justify='center'
                        ).place(
                                 x=265,
                                 y=20,
                                 width=100,
                                 height=30
                                )


# progress bar
progress = ttk.Progressbar(download_frame,
                           orient="horizontal",
                           length=200,
                           mode="determinate",
                           )
                           
progress.place(x=50,y=80,width=600,height=35)
#progress.pack_forget()


# percent label
percent_label_var.set("0%")
percent_label=ttk.Label(download_frame,
                       textvariable=percent_label_var,
                       background='#ADD8E6',
                       foreground='black'
                      )
percent_label.place(x=655,y=80,width=50,height=35)



#######################################################################

#########################################################################
start_stop_frame=tk.Frame(root,bg='',width=410,height=45)
start_stop_frame.place(x=200,y=370)



def updatedata(data):
    #print(data.items())
    downloaded_ratio = int(int(data['downloaded_bytes']) / 1048576)
    filesize_label_var.set(data['_total_bytes_str'])
    speed_label_var.set(str(data['_speed_str']))
    downloaded_label_var.set(str(downloaded_ratio)+'Mb')
    percent_label_var.set(data['_percent_str'])
    filename_label_var.set(data['filename'])
    remaining_time_var.set(data['_eta_str'])
    value=data['_percent_str']
    value=value[:len(value)-1]
    progress["value"] =float(value)
    status_label_var.set(data['status'])
    if data['status'].find('finished')!=-1:
        download_button.configure(state='enable')



# download button
def start_download():
    global curent_file_url
    if code.curent_file_metadata == None:
        return ''
    download_button.configure(state='disable')
    code.options['extractaudio']=audio_var.get()
    code.options['noplaylist']=(code.curent_file_metadata['playlist']!= None) and (video_or_playlist_var.get()== 'playlist')
    #code.options['playliststart']=
    # #code.options['playlistend']=
    code.options['writeautomaticsub']=True if subtitles_var.get()=='yes' else False
    code.options['progress_hooks'] = [updatedata]
    code.init_download(curent_file_url)


download_button=tk.Button(start_stop_frame,
                          text='Start Download',
                          command=start_download,
                          fg='white',
                          bg='blue',
                          relief='flat',
                          )
#download_button.configure(state='disable')
download_button.place(x=10,y=0,width=190,height=45)

def stop_download():
    code.stop_download()
    download_button.configure(state='normal')

# stop button
stop_button=tk.Button(    start_stop_frame,
                          text='Stop',
                          command=stop_download,
                          fg='white',
                          bg='orange',
                          relief='flat',
                          #state='disable'
                          )
stop_button.place(x=210,y=0,width=190,height=45)

##################################################
root.mainloop()
