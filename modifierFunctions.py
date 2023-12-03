from pydub import AudioSegment

def to_mono (filename):
	# initializes a variable for use with Pydub
	original_audio = AudioSegment.from_file(filename, format="wav")
	#sets one channel
	mono_audio = original_audio.set_channels(1)
	# Exports converted file with "mono_" appended beforehand (please change it if it's problematic)
	mono_audio.export("mono_" + filename, format="wav")