from audio_model import Model
from audio_view import View
from audio_controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio Downloader")
        m = Model()
        v = View(self)
        v.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(m, v)
        View.set_controller(v, controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
