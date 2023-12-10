# Audio Graphical Software

Our software allows users to work with any audio file in order to graph out the audio data as a histogram, waveform, and spectrogram, as well as a graph of the low, mid, and high frequencies, including a combined frequencies graph.

---

## Necessary Files
#### `audio_controller.py`
  > Contains the class **Controller** that houses the methods for selecting a file to import, getting the details of the files, and plotting each type of plot with the data.

  > Contains the code that communicates between **Model** and the **View**, receiving user input and deciding what to do with it. 

#### `audio_model.py`
  >  Contains the class **Model** that houses the constructor for audio data, and the methods that ensure an audio file is a mono_channel, .wav file, acquires the data from the file, calculates the RT60 values from the data, and finds target, low, and high frequencies for the frequency graphs.

  > Contains the code that defines how to handle execution of actions.

#### `audio_view.py`
  > Contains the class **View** that houses the constructor for the tkinter GUI components such as the Buttons, Entry section, and Labels as well as organizes them in the window via the grid() method. It also houses the methods that are used by the command parameters in the tkinter widgets.

  > Contains the code that creates the usable features for the program.

#### `mvc_audio.py`
  > Contains the class **App** that executes the tkinter window, creating objects from Controller, Model, and View.

---

## Necessary Modules
The modules (and their versions) that are necessary to run the program from `mvc_audio.py` and are listed in the file `requirements.txt`. A general list of the modules used are listed below:

* matplotlib (*pyplot*)
* numpy
* os
* pydub (*AudioSegment*)
* scipy.io (*wavfile*)
* tkinter (*Text*, *Label*, *filedialog*)
* wave

The files `audio_controller.py`, `audio_model.py`, `audio_view.py` must also be imported into `mvc_audio.py` in order for the program to run.
