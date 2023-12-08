import os
import pydub
from pydub import AudioSegment
import wave
import ffmpeg
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from tkinter import *

# I don't know if the class can be implemented due to the command parameter as a part of the tkinter widgets.
# All the necesary functions are below this commented out portion, I just wanted to keep the class in case we needed it.
"""
class ModifyFile:
    def __init__(self, filename):
        self.filename = filename
    def convert_to_wave(self):
        # Converts the input file to the appropriate extension with the same name
        new_filename = "modified_" + os.path.splitext(self.filename)[0] + '.wav'
        # Loads the audio file
        wav_audio = AudioSegment.from_mp3(self.filename)
        # Exports the file in wav format
        wav_audio.export(new_filename, format="wav")
        self.filename = new_filename

    def to_mono_rem_meta(self):
        # initializes a variable for use with Pydub
        original_audio = AudioSegment.from_file(self.filename, format="wav")
        # sets one channel
        mono_audio = original_audio.set_channels(1)
        # Exports converted file, also removing the metadata (tags).
        mono_audio.export(self.filename, format="wav", tags={})

    def audio_statistics(self):
        samplerate, data = wavfile.read(self.filename)
        # Dictionary of the relevant statistics
        statistics_dict = {'Channels': len(data.shape), 'Sample Rate': samplerate, 'Length': data.shape[0] / samplerate}
        print("Number of Channels: ", statistics_dict['Channels'])
        print("Sample Rate = ", statistics_dict['Sample Rate'], "Hz")
        print("Length = ", statistics_dict['Length'], "s")
        return statistics_dict

    def plot_wav(self, dictionary):
        samplerate, data = wavfile.read(self.filename)
        time = np.linspace(0., dictionary['Length'], data.shape[0])
        plt.plot(time, data[:], label="Visualized Audio")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    def plotHist(self):
        # Creates an object from the Figure class, allows a plot to be in the tkinter GUI
        fig = Figure(figsize=(5, 5), dpi=100)

        rate, data = wavfile.read(self.filename)  # reading wave file.
        c = data[0:9999]

        p = fig.gca()
        p.hist(c, bins='auto')  # arguments are passed to np.histogram.

        canvas = FigureCanvasTkAgg(fig, root)
        canvas.draw()
        canvas.get_tk_widget().pack()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)

def process_file(filename):
    # Faster way to do all the modifications all at once (convert_to_wave has to be the first modification)
    input_file = ModifyFile(filename)
    input_file.convert_to_wave()
    input_file.to_mono_rem_meta()
    input_file.plot_wav(input_file.audio_statistics())
"""


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)


# get method for use with the functions that need the filename.
def getFile():
    return entry.get()


def convert_to_wave():
    filename = getFile()
    # Converts the input file to the appropriate extension with the same name
    new_filename = os.path.splitext(filename)[0] + '.wav'
    # Loads the audio file
    wav_audio = AudioSegment.from_mp3(filename)
    # Exports the file in wav format
    wav_audio.export(new_filename, format="wav")


def to_mono():
    convert_to_wave()
    self = os.path.splitext(getFile())[0] + '.wav'
    # initializes a variable for use with Pydub
    original_audio = pydub.AudioSegment.from_file(self, format="wav")
    global mod_file_name
    new_filename = os.path.splitext(self)[0] + '_modified.wav'
    mod_file_name = new_filename
    # sets one channel
    mono_audio = original_audio.set_channels(1)
    # Exports converted file, and also removes metadata (tags).
    mono_audio.export(new_filename, format="wav", tags={}, )
    # Test to see if is worked
    result = os.path.exists(new_filename)
    print(result)


def print_details():
    new_wav = pydub.AudioSegment.from_file(file=mod_file_name, format="wav")
    T.insert(tk.END, "Time: " + str(len(new_wav)) + "\nChannels " + str(new_wav.channels) + "\nMax Amplitude " + str(new_wav.max))


def plot_wav():
    filename = mod_file_name
    spf = wave.open(filename, "r")
    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    print(type(signal))
    signal = np.fromstring(signal, "int16")
    fs = spf.getframerate()

    time = np.linspace(0, len(signal) / fs, num=len(signal))

    plt.figure(1)
    plt.title("Signal Wave...")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.plot(time, signal)
    plt.show()


# create a function that can get the file name for use in plotHist
# or other graphing things
def plotHist():
    filename = mod_file_name
    # Creates an object from the Figure class, allows a plot to be in the tkinter GUI
    fig = Figure(figsize=(5, 5), dpi=100)

    rate, data = wavfile.read(filename)  # reading wave file.
    c = data[0:9999]

    p = fig.gca()
    p.hist(c, bins='auto')  # arguments are passed to np.histogram.

    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().pack()


# For testing purposes
root = tk.Tk()
root.title("Audio Downloader")
root.resizable(False, False)
root.geometry('600x600')

select_button = tk.Button(root, text="Select File", command=select_file)


entry = tk.Entry(root, width=50)


download_button = tk.Button(root, text="Download", command=to_mono)


details_button = tk.Button(root, text="Details", command=print_details)


status_label = tk.Label(root, text="")


plot_hist_button = tk.Button(master=root, command=plotHist, text="Plot Histogram")


plot_graph_button = tk.Button(master=root, command=plot_wav, text="Plot Graph")

# Create text widget and specify size.
T = Text(root, height=5, width=52)
# Create detail_label
detail_label = Label(root, text="Details")
detail_label.config(font=("Courier", 14))
# Exit Button
quit_button = Button(root, text="Exit",command=root.destroy)


# Button Packing Order
select_button.pack()
entry.pack()
download_button.pack()
detail_label.pack()
T.pack()
details_button.pack()
status_label.pack()
plot_hist_button.pack()
plot_graph_button.pack()
quit_button.pack()

# Run Program
root.mainloop()
