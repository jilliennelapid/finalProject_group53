from tkinter import filedialog


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.view.select_file(file_path)

    def download(self, file):
        try:
            self.model.to_mono(file)
        except OSError as e:
            self.view.show_error()

    def print_details(self):
        try:
            self.model.get_data()
            self.model.find_rt60()
            time = self.model.time
            channels = self.model.channels
            res = self.model.res
            rt60 = self.model.rt60
            self.view.print_details(time, channels, res, rt60)
        except AttributeError as e:
            self.view.show_error()

    def plot_wav(self):
        try:
            self.model.get_waveform_data()
            t = self.model.waveform_time
            s = self.model.signal
            self.view.plot_wav(t, s)
        except AttributeError as e:
            self.view.show_error()

    def plot_spectrogram(self):
        try:
            self.model.get_spec_data()
            sample = self.model.sample_r
            data = self.model.data
            self.view.plot_spectrogram(sample, data)
        except TypeError as e:
            self.view.show_error()

    def plot_mid_freq(self):
        try:
            gt = self.model.graph_time
            self.model.frequency_check(1)
            db = self.model.data_in_db_fun
            self.view.plot_mid_freq(gt, db)
        except TypeError as e:
            self.view.show_error()

    def plot_low_freq(self):
        try:
            gt = self.model.graph_time
            self.model.frequency_check(2)
            db = self.model.data_in_db_fun
            self.view.plot_low_freq(gt, db)
        except TypeError as e:
            self.view.show_error()

    def plot_high_freq(self):
        try:
            gt = self.model.graph_time
            self.model.frequency_check(3)
            db = self.model.data_in_db_fun
            self.view.plot_high_freq(gt, db)
        except TypeError as e:
            self.view.show_error()

    def combined_frequency(self):
        try:
            gt = self.model.graph_time
            self.model.frequency_check(2)
            db_low = self.model.data_in_db_fun
            self.model.frequency_check(1)
            db_mid = self.model.data_in_db_fun
            self.model.frequency_check(3)
            db_high = self.model.data_in_db_fun
            self.view.combined_frequency(gt, db_low, db_mid, db_high)
        except TypeError as e:
            self.view.show_error()

    def plot_hist(self):
        try:
            self.model.get_spec_data()
            data = self.model.data
            self.view.plot_hist(data)
        except TypeError as e:
            self.view.show_error()