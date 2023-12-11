# Audio Graphical Software

Our software allows users to work with any audio file in order to graph out the audio data as a histogram, waveform, and spectrogram, as well as a graph of the low, mid, and high frequencies, including a combined frequencies graph.

---
## Table of Contents
* [Necessary Files](#files)
* [Necessary Modules](#modules)
* [Installation and Running Instructions](#instructions)
* [Usage Instructions](#how-to-use)

---
<a name="files"></a>
## Necessary Files
#### [`audio_controller.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_controller.py)
  > Contains the class **Controller** that houses the methods for selecting a file to import, getting the details of the files, and plotting each type of plot with the data.

  > Contains the code that communicates between **Model** and the **View**, receiving user input and deciding what to do with it. 

#### [`audio_model.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_model.py)
  >  Contains the class **Model** that houses the constructor for audio data, and the methods that ensure an audio file is a mono_channel, .wav file, acquires the data from the file, calculates the RT60 values from the data, and finds target, low, and high frequencies for the frequency graphs.

  > Contains the code that defines how to handle execution of actions.

#### [`audio_view.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_view.py)
  > Contains the class **View** that houses the constructor for the tkinter GUI components such as the Buttons, Entry section, and Labels as well as organizes them in the window via the grid() method. It also houses the methods that are used by the command parameters in the tkinter widgets.

  > Contains the code that creates the usable features for the program.

#### [`mvc_audio.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/mvc_audio.py)
  > Contains the class **App** that executes the tkinter window, creating objects from Controller, Model, and View.

---
<a name="modules"></a>
## Necessary Modules
The modules (and their versions) that are necessary to run the program from are listed in the file [`requirements.txt`](https://github.com/jilliennelapid/finalProject_group53/edit/main/requirements.txt). A general list of the modules used, as well as links to their documentations, are listed below:

* [matplotlib](https://matplotlib.org/stable/index.html) (*pyplot*)
* [numpy](https://numpy.org/doc/)
* [os](https://docs.python.org/3/library/os.html)
* [pydub](https://github.com/jiaaro/pydub) (*AudioSegment*)
* [scipy.io](https://docs.scipy.org/doc/) (*wavfile*)
* [tkinter](https://docs.python.org/3/library/tk.html) (*Text*, *Label*, *filedialog*)
* [wave](https://docs.python.org/3/library/wave.html)

The files [`audio_controller.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_controller.py), [`audio_model.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_model.py), [`audio_view.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/audio_view.py) must also be imported into [`mvc_audio.py`](https://github.com/jilliennelapid/finalProject_group53/blob/main/mvc_audio.py) in order for the program to run.

---
<a name="instructions"></a>
## Installation and Running Instructions
1) Attain the files `audio_controller.py`, `audio_model.py`, `audio_view.py`, and `mvc_audio.py` via forking

    **OR** by downloading the specified files to a local repository.
2) Open up Command Prompt and use `cd` to get into the directory/folder where you downloaded the source code.
3) Use `python -m venv .venv` to create a virtual environment if you don't want to download all the Python modules globally on your computer. (Syntax may vary for different terminals or operating systems)
4) Use `.\.venv\Scripts\activate` to activate the virtual environment. (Syntax may vary for different terminals or operating systems)
5) Install all the modules to the virtual environment with `pip install -r requirements.txt`.
6) Run the program with `python mvc_audio.py` or `python3 mvc_audio.py`
---
<a name="how-to-use"></a>
## Usage Instructions
* Importing a audio file
  > After opening the program, press the `Select File` button in order to open your File Explorer/Finder. Select the audio file you wish to import into the software. Any audio file type is allowed (.mp3, .mp4, .wav, etc.).
  
  > After selecting the file, ensure that you press `Download` for the software to convert the file to .wav and store it for use in the program.

* Seeing statistics (details) of the file
  > After a file has been downloaded, press the `Details` button to see statistics such as Time, Channels, Resonance, and RT60 Difference.

* Displaying a graph of the audio data
  > After a file has been downloaded, you can select any of the "Plot" buttons to plot the data, such as `Plot Spectrogram` or `Plot Combined Frequency`. This will cause a separate window to appear with the desired graph. Closing the separate plot window will not close the program.

  > Multiple graphs can be opened at the same time.
  
* Closing the program
  > To close the program at any time make use of the `X` button built into the window or the `Exit` button at the top right of the program.
