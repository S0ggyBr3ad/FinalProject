import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal as sp_sig
import wave

# All methods for analysing the file
class Reverb:
    # Initializes variables
    def __init__(self):
        self.sample_rate = None
        self.data = None
        self.spectrum = None
        self.freqs = None
        self.t = None
        self.im = None
        self.data_in_db = None
        self.range = None
        self.RT60 = None

    # Opens the wav file and sets some variables for later use
    def openFile(self, filename):
        self.sample_rate, self.data = wavfile.read(filename)
        self.spectrum, self.freqs, self.t, self.im = plt.specgram(self.data, Fs=self.sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
        plt.clf()

    # Returns the length of the file in seconds
    def getTime(self):
        return self.t[len(self.t)-1]

    # Takes the frequency range (low, mid, high) and returns an index of the dB values
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

    # Creates the spectrogram graph
    def specgram(self):
        plt.specgram(self.data, Fs=self.sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    # Creates a dB vs time graph based on the frequency (low, mid, high)
    def dbplt(self, ranges):
        self.frequency_check(ranges)

        # Changes the color of the graph based on the predetermined frequency values
        if 0 < ranges <= 200:
            color = "#0000FF"
        elif 200 < ranges <= 2000:
            color = "#00FF00"
        else:
            color = "#FF0000"

        # Plot dB vs time and label axes
        plt.plot(self.t, self.data_in_db, linewidth=1, alpha=0.7, color=color)
        plt.xlabel('Time (s)')
        plt.ylabel('Power (dB)')

        # Take the frequency (low, mid, high), calculate the RT20, and extrapolate for the RT60
    def getRT60(self, ranges):
        self.frequency_check(ranges)
        index_of_max = np.argmax(self.data_in_db)

        value_of_max = self.data_in_db[index_of_max]

        # slice array from a max value
        sliced_array = self.data_in_db[index_of_max:]

        value_of_max_less_5 = value_of_max - 5
        value_of_max_less_5 = self.find_nearest_value(sliced_array, value_of_max_less_5)

        index_of_max_less_5 = np.where(self.data_in_db == value_of_max_less_5)


        # slice array from a max -5dB
        value_of_max_less_25 = value_of_max - 25

        value_of_max_less_25 = self.find_nearest_value(sliced_array, value_of_max_less_25)

        index_of_max_less_25 = np.where(self.data_in_db == value_of_max_less_25)

        rt20 = (self.t[index_of_max_less_5] - self.t[index_of_max_less_25])[0]

        # extrapolate rt20 to rt60
        self.RT60 = round(abs(3*rt20), 2)

        return self.RT60

    # Returns the frequency (low, mid, high) at which the peak dB value is reached. Used for calculating overall RT60
    def getMaxDBFreq(self):
        self.frequency_check(200)
        low_max_db = self.data_in_db[np.argmax(self.data_in_db)]
        self.frequency_check(1000)
        mid_max_db = self.data_in_db[np.argmax(self.data_in_db)]
        self.frequency_check(4000)
        high_max_db = self.data_in_db[np.argmax(self.data_in_db)]
        if low_max_db > mid_max_db and low_max_db > high_max_db:
            return 200
        elif mid_max_db > high_max_db:
            return 1000
        else:
            return 4000

    # Calls the getRT60() method with the frequency at which the peak dB value occurs, based on the getMaxDBFreq() method
    def getCombinedRT60(self):
        return self.getRT60(self.getMaxDBFreq())

    # Uses welch to find the resonant frequency
    def getResonantFreq(self):
        frequencies, power = sp_sig.welch(self.data, self.sample_rate, nperseg=4096)
        dominant_frequency = frequencies[np.argmax(power)]
        return round(dominant_frequency)

    # Plots the waveform of the sound file
    def waveformplt(self):
        waveform = wave.open("pt_mono.wav", "r")
        raw = waveform.readframes(-1)
        raw = np.frombuffer(raw, "int16")
        plt.title("Waveform")
        plt.plot(raw, color="#FF9999")