from pydub import AudioSegment


def remove_metadata(input_wav, output_wav):
    # Load the input wav file using pydub
    audio = AudioSegment.from_wav(input_wav)

    # Export the initial wav file without metadata.
    # output_wave is the new name of the file with the removed metadata.
    audio.export(output_wav, format="wav", tags={})


if __name__ == "__main__":
    # within the quotes would be the file name of the initial file we're using
    # then the file name of the modified initial file with the metadata removed.
    input_wav_file = ""
    output_wav_file = ""

    remove_metadata(input_wav_file, output_wav_file)
