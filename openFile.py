import os
import pydub
from pydub import AudioSegment


class ModifyFile:
    def convert_to_wave(self, input_file):
        # Converts the input file to the appropriate extension with the same name
        wave_file = os.path.splitext(input_file)[0] + '.wav'
        # Loads the audio file
        sound = pydub.AudioSegment.from_mp3(input_file)
        # Exports the file in wav format
        sound.export(wave_file, format="wav")
        print("Conversion Complete")

    def to_mono(self, filename):
        # initializes a variable for use with Pydub
        original_audio = AudioSegment.from_file(filename, format="wav")
        # sets one channel
        mono_audio = original_audio.set_channels(1)
        # Exports converted file with "mono_" appended beforehand (please change it if it's problematic)
        mono_audio.export("mono_" + filename, format="wav")

    def remove_metadata(self, input_wav, output_wav):
        # Load the input wav file using pydub
        audio = AudioSegment.from_wav(input_wav)

        # Export the initial wav file without metadata.
        # output_wave is the new name of the file with the removed metadata.
        audio.export(output_wav, format="wav", tags={})


# this is just making use of the method remove_metadata in an example situation
if __name__ == "__main__":
    # within the quotes would be the file name of the initial file we're using
    # then the file name of the modified initial file with the metadata removed.
    input_wav_file = ""
    output_wav_file = ""

    mod = ModifyFile()
    mod.remove_metadata(input_wav_file, output_wav_file)