import os
import pydub
from pydub import AudioSegment
import wave
import ffmpeg

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

	def audio_duration(self):
		audio = AudioSegment.from_file(self.filename, format="wav")
		return audio.duration_seconds

def process_file(filename):
	# Faster way to do all the modifications all at once (convert_to_wave has to be the first modification)
	input_file = ModifyFile(filename)
	input_file.convert_to_wave()
	input_file.to_mono()
	input_file.remove_metadata()
	print("duration:", str(input_file.audio_duration()))



# For testing purposes
testFile = ""
process_file(testFile)