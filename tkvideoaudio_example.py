# to install tkvideoaudio, 
# so that you won't need the tkvideoaudio.py file in the folder of the example:
# pip install tkvideoaudio@git+https://github.com/formazione/tkvideoaudio

import tkinter as tk
from tkvideoaudio import tkvideo
import pygame


root = tk.Tk()
root.title("video play")
label_video=tk.Label(root)
label_video.pack()
video_file=tkvideo("001.mp4",label_video,loop=1,size=(800,600))
video_file.play()
root.mainloop()
pygame.quit()