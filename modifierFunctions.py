from pydub import AudioSegment

def to_mono (filename):
	# initializes a variable for use with Pydub
	original_audio = AudioSegment.from_file(filename, format="wav")
	#sets one channel
	mono_audio = original_audio.set_channels(1)
	# Exports converted file with "mono_" appended beforehand (please change it if it's problematic)
	filename = "mono_" + filename
	mono_audio.export(filename, format="wav")
	return filename

wav_file = '16bit2chan.wav'
wav_file = to_mono(wav_file)
print(wav_file)
