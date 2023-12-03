# ffmpeg must be downloaded to run properly
import os
import pydub


def convert_to_wave(input_file):
    # Converts the input file to the appropriate extension with the same name
    wave_file = os.path.splitext(input_file)[0] + '.wav'
    # Loads the audio file
    sound = pydub.AudioSegment.from_mp3(input_file)
    # Exports the file in wav format
    sound.export(wave_file, format="wav")
    print("Conversion Complete")