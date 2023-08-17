# this example uses tkvideo and the start_audio function
# to add audio to the video, because tkvideo do not
# has this function
# you can use the tkvideoaudio module avoid putting the stat_audio function in the code
# pip install tkvideoaudio@git+https://github.com/formazione/tkvideoaudio
# then substitute the import of tkvideo with:
# from tkvideoaudio import tkvideo


import tkinter as tk
from tkvideo import tkvideo
import os

if "audio.mp3" not in os.listdir():
    os.system("ffmpeg -i 001.mp4 audio.mp3")


def start_audio():
    import pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()


root = tk.Tk()
root.title("video play")
label_video=tk.Label(root)
label_video.pack()
video_file=tkvideo("001.mp4",label_video,loop=1,size=(800,600))
video_file.play()
start_audio()
root.mainloop()



