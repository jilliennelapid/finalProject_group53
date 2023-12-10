# Change Log
All notable changes to this project will be documented in this file.

## [1.0] - 2023-12-10
### Added
Created files audio_controller.py, audio_model.py, audio_view.py, and mvc_audio.py that separates the existent code into classes specialized for getting data from the audio file and graphing the data, initialling importing the audio file and attain details such as frequency and RT60 values, creating the tkinter GUI, and running the entire program, respectively.

### Changed
Removed beta file openFile.py from the main branch as the newly formatted MVC files replaced the file.

### Fixed
Finalized all methods for graphing, the tkinter GUI code, all methods for working with the audio files.

## [0.6] - 2023-12-09
### Added
From daveDev, added methods for graphing the low, mid, and high frequencies as well as calculating the RT60 values from the audio files.
Formalized the details display label to display time, length, channes, and RT60 value.

### Changed
From jillDev, tried to embedded all plots into the tkinter GUI as well as edited the layout of the tkinter GUI.

### Fixed


## [0.5] - 2023-12-07
### Added
From jillDev and then to main branch, combined the methods created for working with the audio files, creating the tkinter GUI, and creating the plots and embedding them into tkinter into openFile.py.
In branch daveDev, added new tkinter buttons for the new methods for graphing a spectrogram and mixed frequencies.

### Changed


### Fixed
Fixed one method for graphing a basic plot and executing it from the tkinter GUI.

## [0.4] - 2023-12-06
### Added
In branch development, model.py file added that contains methods to execute all methods and a method that returns audio duration.
In branch daveDev, created a method that downloads audio files into the tkinter program.

### Changed


### Fixed
Cleans up some of the implementation from openFile.py code.

## [0.3] - 2023-12-05
### Added


### Changed
Condensed the .py files in the branches into openFile.py in main branch and created a class that contains all functions
related to opening a file, converting the file to .wav, getting a single channel from the file, and removing audio file metadata.

### Fixed


## [0.2] - 2023-12-03
### Added
Added three additional branches in order to push different .py files: development, daveDev, and jillDev.

### Changed
Added modules used on 2023-12-03 to requirements.txt.

### Fixed


## [0.1] - 2023-12-02
### Added
Added the files README.md, CHANGELOG.md, requirements.txt, setup.cfg, and openFile.py.

### Changed
Added descriptions to the markdown files.

### Fixed
