import tkinter as tk
from tkinter import filedialog
import shutil
import os
import pydub
#from model import *


wav_file = pydub.AudioSegment.from_file(file="16bit1chan.wav", format="wav")


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)


# Obsolete
def download_audio():
    src_file = entry.get()
    if src_file:
        try:
            file_name = os.path.basename(src_file)
            shutil.copy2(src_file, file_name)
            status_label.config(text=f"Downloaded as {file_name}")
        except FileNotFoundError:
            status_label.config(text="Error: File not found")
    else:
        status_label.config(text="Please select a file")


def to_mono():
    self = entry.get()
    # initializes a variable for use with Pydub
    original_audio = pydub.AudioSegment.from_file(self, format="wav")
    global mod_file_name
    new_filename = os.path.splitext(self)[0] + '_modified.wav'
    mod_file_name = new_filename
    # sets one channel
    mono_audio = original_audio.set_channels(1)
    # Exports converted file
    mono_audio.export(new_filename, format="wav", tags={}, )
    result = os.path.exists(new_filename)
    print("--------------")
    print(result)


def print_details():
    new_wav = pydub.AudioSegment.from_file(file=mod_file_name, format="wav")
    #file type
    print(type(new_wav))
    #  To find frame rate of song/file
    print(new_wav.frame_rate)
    # To know about channels of file
    print(new_wav.channels)
    # Find the number of bytes per sample
    print(new_wav.sample_width)
    # Find Maximum amplitude
    print(new_wav.max)
    # To know length of audio file
    print(len(new_wav))


root = tk.Tk()
root.title("Audio Downloader")
root.resizable(False, False)
root.geometry('500x500')

select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack()

entry = tk.Entry(root, width=50)
entry.pack()

download_button = tk.Button(root, text="Download", command=to_mono)
download_button.pack()

details_button = tk.Button(root, text="Details", command=print_details)
details_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()