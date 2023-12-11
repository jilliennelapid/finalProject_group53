import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Text
from tkinter import Label


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Download Buttons
        self.select_button = tk.Button(self, text="Select File", command=self.select_file_click)
        self.entry = tk.Entry(self, width=50)
        self.download_button = tk.Button(self, text="Download", command=self.download)

        # Details Button
        self.details_button = tk.Button(self, text="Details", command=self.print_details_click)
        # Create text widget and specify size.
        self.T = Text(self, height=5, width=52)
        # Create detail_label
        self.detail_label = Label(self, text="Details")
        self.detail_label.config(font=("Courier", 14))

        # Graph Buttons
        self.plot_hist_button = tk.Button(master=self, command=self.plot_hist_click, text="Plot Histogram")
        self.plot_graph_button = tk.Button(master=self, command=self.plot_wav_click, text="Plot Waveform")
        self.spectrogram_button = tk.Button(master=self, command=self.plot_spectrogram_click, text="Plot Spectrogram")
        self.mid_frequency_button = tk.Button(master=self, command=self.plot_mid_freq_click, text="Plot Mid Frequency")
        self.low_frequency_button = tk.Button(master=self, command=self.plot_low_freq_click, text="Plot Low Frequency")
        self.high_frequency_button = tk.Button(master=self, command=self.plot_high_freq_click, text="Plot High Frequency")
        self.combined_frequency_button = tk.Button(master=self, command=self.combined_frequency_click, text="Plot Combined Frequency")
        self.quit_button = tk.Button(self, text="Exit", command=parent.destroy)

        self.select_button.grid(row=0, column=1)
        self.entry.grid(row=1, column=1)
        self.download_button.grid(row=2, column=1)
        self.detail_label.grid(row=3, column=1)
        self.T.grid(row=4, column=1)
        self.details_button.grid(row=5, column=1)
        self.plot_hist_button.grid(row=6, column=0)
        self.plot_graph_button.grid(row=6, column=1)
        self.spectrogram_button.grid(row=6, column=2)
        self.low_frequency_button.grid(row=7, column=0)
        self.mid_frequency_button.grid(row=7, column=1)
        self.high_frequency_button.grid(row=7, column=2)
        self.combined_frequency_button.grid(row=8, column=1)
        self.quit_button.grid(row=0, column=2)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def select_file_click(self):
        if self.controller:
            self.controller.select_file()

    def select_file(self, file):
        if file:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, file)

    def download(self):
        if self.controller:
            self.controller.download(self.entry.get())

    def print_details_click(self):
        if self.controller:
            self.controller.print_details()

    def print_details(self, time, channels, res, rt60):
        if self.controller:
            self.T.delete("1.0", "end")
            self.T.insert(tk.END, "Time(seconds): " + time + "\nChannels " + channels + "\nResonance(Hz): " + res + "\nRT60 Difference: " + rt60)

    def plot_hist_click(self):
        if self.controller:
            self.controller.plot_hist()

    # create a function that can get the file name for use in plotHist
    # or other graphing things
    def plot_hist(self, data):
        if self.controller:
            c = data[0:9999]
            h_comb_freq = plt.figure("Histogram", clear=True)
            plt.hist(c, bins='auto')
            plt.title("Histogram")
            plt.xlabel("Amplitude [HZ]")
            plt.ylabel("Frequency of Amplitude Value")
            plt.grid()
            h_comb_freq.show()

    def plot_wav_click(self):
        if self.controller:
            self.controller.plot_wav()

    def plot_wav(self, t, s):
        if self.controller:
            g_wav = plt.figure("Waveform", clear=True)
            plt.title("Signal Wave")
            plt.xlabel("Time [s]")
            plt.ylabel("Amplitude [HZ]")
            plt.plot(t, s)
            g_wav.show()

    def plot_spectrogram_click(self):
        if self.controller:
            self.controller.plot_spectrogram()

    def plot_spectrogram(self, sample_r, data):
        if self.controller:
            g_spec = plt.figure("Spectrogram", clear=True)
            spectrum, freqs, t, im = plt.specgram(data, Fs=sample_r, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
            cbar = plt.colorbar(im)
            plt.title("Spectrogram")
            plt.xlabel('Time (s)')
            plt.ylabel('Frequency (Hz)')
            cbar.set_label('Intensity (dB)')
            g_spec.show()

    def plot_mid_freq_click(self):
        if self.controller:
            self.controller.plot_mid_freq()

    def plot_mid_freq(self, gt, data_db):
        if self.controller:
            g_mid_freq = plt.figure("Mid Frequency Graph", clear=True)
            plt.plot(gt, data_db, alpha=0.7, color='#004bc6')
            plt.title("Mid Frequency")
            plt.xlabel('Time (s)')
            plt.ylabel('Power (db)')
            plt.grid()
            g_mid_freq.show()

    def plot_low_freq_click(self):
        if self.controller:
            self.controller.plot_low_freq()

    def plot_low_freq(self, gt, data_db):
        if self.controller:
            g_low_freq = plt.figure("Low Frequency Graph", clear=True)
            plt.plot(gt, data_db, alpha=0.7, color='#6FEC13')
            plt.title("Low Frequency")
            plt.xlabel('Time (s)')
            plt.ylabel('Power (db)')
            plt.grid()
            g_low_freq.show()

    def plot_high_freq_click(self):
        if self.controller:
            self.controller.plot_high_freq()

    def plot_high_freq(self, gt, data_db):
        if self.controller:
            g_high_freq = plt.figure("High Frequency Graph", clear=True)
            plt.plot(gt, data_db, alpha=0.7, color='#F58E11')
            plt.title("High Frequency")
            plt.xlabel('Time (s)')
            plt.ylabel('Power (db)')
            plt.grid()
            g_high_freq.show()

    def combined_frequency_click(self):
        if self.controller:
            self.controller.combined_frequency()

    def combined_frequency(self, gt, db_low, db_mid, db_high):
        if self.controller:
            g_comb_freq = plt.figure("Combined Frequency Graph", clear=True)
            plt.plot(gt, db_high, alpha=0.7, color='#F58E11')
            plt.plot(gt, db_mid, alpha=0.7, color='#004bc6')
            plt.plot(gt, db_low, alpha=0.7, color='#6FEC13')
            plt.title("Combined Frequency")
            plt.xlabel('Time (s)')
            plt.ylabel('Power (db)')
            plt.grid()
            g_comb_freq.show()

    def show_error(self):
        self.T.delete("1.0", "end")
        self.T.insert(tk.END, "Error: File not Downloaded")
