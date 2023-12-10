import os
import pydub
from pydub import AudioSegment
import wave
import ffmpeg
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np


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

	def to_mono(self):
		# initializes a variable for use with Pydub
		original_audio = AudioSegment.from_file(self.filename, format="wav")
		# sets one channel
		mono_audio = original_audio.set_channels(1)
		# Exports converted file
		mono_audio.export(self.filename, format="wav")


	def remove_metadata(self):
		# Load the input wav file using pydub
		audio = AudioSegment.from_wav(self.filename)
		# Export the wav file without metadata.
		audio.export(self.filename, format="wav", tags={})

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


def process_file(filename):
	# Faster way to do all the modifications all at once (convert_to_wave has to be the first modification)
	input_file = ModifyFile(filename)
	input_file.convert_to_wave()
	input_file.to_mono()
	input_file.remove_metadata()
	input_file.plot_wav(input_file.audio_statistics())


# For testing purposes
testFile = ""
process_file(testFile)
