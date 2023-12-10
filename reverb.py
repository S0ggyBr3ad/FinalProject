import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class Reverb:
    def __init__(self):
        self.spectrum = None
        self.freqs = None
        self.t = None
        self.im = None
        self.data_in_db = None
        self.range = None
        self.RT60 = None

    def openFile(self, filename):
        sample_rate, data = wavfile.read(filename)
        self.spectrum, self.freqs, self.t, self.im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
        plt.clf()

    def getTime(self):
        return self.t[len(self.t)-1]

    def frequency_check(self, ranges):
        index_of_frequency = np.where(self.freqs >= ranges)[0][0]
        data_for_frequency = self.spectrum[index_of_frequency]
        # change a digital signal for a values in decibels
        self.data_in_db = 10 * np.log10(data_for_frequency)

    # find a nearest value
    def find_nearest_value(self, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    def dbplt(self, ranges):
        self.frequency_check(ranges)
        plt.figure(2)
        # plot reverb time on grid
        plt.plot(self.t, self.data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
        plt.xlabel('Time (s)')
        plt.ylabel('Power (dB)')

        # find an index of a  max value
        index_of_max = np.argmax(self.data_in_db)

        value_of_max = self.data_in_db[index_of_max]

        plt.plot(self.t[index_of_max], self.data_in_db[index_of_max], 'go')

        # slice array from a max value
        sliced_array = self.data_in_db[index_of_max:]

        value_of_max_less_5 = value_of_max - 5
        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_5)

        index_of_max_less_5 = np.where(self.data_in_db == value_of_max_less_5)

        plt.plot(self.t[index_of_max_less_5], self.data_in_db[index_of_max_less_5], 'yo')

        # slice array from a max -5dB
        value_of_max_less_25 = value_of_max - 25

        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)

        index_of_max_less_25 = np.where(self.data_in_db == value_of_max_less_25)

        plt.plot(self.t[index_of_max_less_25], self.data_in_db[index_of_max_less_25], 'ro')
        rt20 = (self.t[index_of_max_less_5] - self.t[index_of_max_less_25])[0]

        # extrapolate rt20 to rt60
        self.RT60 = 3*rt20

        # optional set limits on plot
        return plt
