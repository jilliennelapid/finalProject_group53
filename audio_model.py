import os
import pydub
from pydub import AudioSegment
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


class Model:
    def __init__(self):
        self.entry = None
        self.mod_file_name = None
        self.graph_freq = None
        self.graph_spec = None
        self.graph_time = None
        self.target_frequency = None

        self.time = None
        self.channels = None
        self.res = None
        self.rt60 = None

        self.waveform_time = None
        self.signal = None

        self.sample_r = None
        self.data = None

        self.data_in_db_fun = None

    def convert_to_wave(self):
        filename = self.entry
        # Converts the input file to the appropriate extension with the same name
        new_filename = os.path.splitext(filename)[0] + '.wav'
        # Loads the audio file
        wav_audio = AudioSegment.from_file(filename)
        # Exports the file in wav format
        wav_audio.export(new_filename, format="wav")

    def to_mono(self, file):
        self.entry = file
        self.convert_to_wave()
        se = os.path.splitext(self.entry)[0] + '.wav'
        # initializes a variable for use with Pydub
        original_audio = pydub.AudioSegment.from_file(se, format="wav")
        new_filename = os.path.splitext(se)[0] + '_modified.wav'
        self.mod_file_name = new_filename
        # sets one channel
        mono_audio = original_audio.set_channels(1)
        # Exports converted file, and also removes metadata (tags).
        mono_audio.export(new_filename, format="wav", tags={}, )

        # Creates necessary info for other functions
        filename = self.mod_file_name
        sample_rate, data = wavfile.read(filename)
        spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
        self.graph_freq = freqs
        self.graph_spec = spectrum
        self.graph_time = t

    def find_rt60(self):
        self.rt60 = str(((self.find_local_rt60(1) + self.find_local_rt60(2) + self.find_local_rt60(3)) / 3) - 0.5)

    def get_data(self):
        a = pydub.AudioSegment.from_file(file=self.mod_file_name, format="wav")
        self.time = str(len(a) / 1000)
        self.channels = str(a.channels)
        self.res = str(a.max)

    def get_waveform_data(self):
        filename = self.mod_file_name
        spf = wave.open(filename, "r")
        # Extract Raw Audio from Wav File
        self.signal = spf.readframes(-1)
        self.signal = np.fromstring(self.signal, "int16")
        fs = spf.getframerate()
        self.waveform_time = np.linspace(0, len(self.signal) / fs, num=len(self.signal))

    def get_spec_data(self):
        filename = self.mod_file_name
        self.sample_r, self.data = wavfile.read(filename)

    def frequency_check(self, gate):
        # identify a freq to check
        if gate == 1:
            self.target_frequency = self.find_target_frequency(self.graph_freq)
        if gate == 2:
            self.target_frequency = self.find_low_frequency(self.graph_freq)
        if gate == 3:
            self.target_frequency = self.find_high_frequency(self.graph_freq)
        index_of_frequency = np.where(self.graph_freq == self.target_frequency)[0][0]
        # find sound data
        data_for_frequency = self.graph_spec[index_of_frequency]
        # change a digital signal for a values in decibels
        data_in_db_fun = 10 * np.log10(data_for_frequency)
        self.data_in_db_fun = data_in_db_fun
        return data_in_db_fun

    def find_local_rt60(self, i):
        data_in_db = self.frequency_check(i)
        # find an index of max value
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]

        # slice the array from a max value
        sliced_array = data_in_db[index_of_max:]
        value_of_max_less_5 = value_of_max - 5

        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)

        # slice array from a max -5db
        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

        rt20 = (self.graph_time[index_of_max_less_5] - self.graph_time[index_of_max_less_25])[0]

        # print
        rt60 = 3 * rt20
        a = round(abs(rt60), 2)
        return a

    @staticmethod
    def find_target_frequency(freq):
        for x in freq:
            if x > 1000:
                break
        return x

    @staticmethod
    def find_low_frequency(freq):
        for x in freq:
            if x > 250:
                break
        return x

    @staticmethod
    def find_high_frequency(freq):
        for x in freq:
            if x > 5000:
                break
        return x

    @staticmethod
    def find_nearest_value(array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]