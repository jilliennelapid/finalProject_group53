from scipy.io import wavfile
import scipy.io

# file name would need to be read and saved to this variable
wav_fname = ""

# opens the .wav file
samplerate, data = wavfile.read(wav_fname)

print(f"number of channels = {data.shape[len(data.shape) - 1]}")
print(f"sample rate = {samplerate}Hz")

length = data.shape[0] / samplerate
print(f"length = {length}s")