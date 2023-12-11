import os.path
from tkinter import *
from tkinter import ttk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from convert import *
from reverb import *

# Initialize class variable to call methods from
reverb = Reverb()

# Handles getting the file from user and calls conversion functions
def selectFile():
    filename = askopenfilename(filetypes=(("wav File", "*.wav"), ("mp3 File", "*.mp3")))
    if filename.endswith(".wav"):
        toMono(filename)
    elif filename.endswith(".mp3"):
        mp3towav(filename)
        toMono("pt_mono.wav")
    else:
        filename_label.config(text="Please choose a .mp3 or .wav file.")
        return

    # Enables graph buttons when acceptable file is selected
    lowRT60Btn.config(state="normal")
    midRT60Btn.config(state="normal")
    highRT60Btn.config(state="normal")
    combRT60Btn.config(state="normal")
    waveformBtn.config(state="normal")
    spectBtn.config(state="normal")

    # Opens the file
    reverb.openFile("pt_mono.wav")

    # Displays the name, length, resonant frequency, and RT60 of the selected file
    filename_label.config(text=f"Current file: {os.path.basename(filename)}")
    time_label.config(text=f"{round(reverb.getTime(), 2)} seconds.")
    ResonantFrequency_label.config(text=f"Resonant frequency: {reverb.getResonantFreq()} Hz")
    updateRT60(reverb.getCombinedRT60())

# Used to change the RT60 value displayed in the tkinter window
def updateRT60(RT60):
    RT60_label.config(text=f"The RT60 is {RT60} seconds.")
    RT60diff_label.config(text=f"The RT60 diff is {round(RT60-0.5, 2)}")

# Tkinter stuff
root = Tk()
root.title('S. P. I. D. A. M.')
root.geometry("200x278")

_mainframe = ttk.Frame(root, padding='5 5 5 5 ')
_mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S"))

# All labels
textFrame = ttk.Frame(root, relief='sunken')
textFrame.grid(row = 2, column = 0, sticky=("E", "W", "S"))
textFrame = ttk.LabelFrame(_mainframe, text = '')

filename_label = ttk.Label(_mainframe, text = '')
filename_label.grid(row = 2, column = 0)

time_label = ttk.Label(_mainframe, text = '')
time_label.grid(row = 3, column = 0)

RT60_label = ttk.Label(_mainframe, text = '')
RT60_label.grid(row = 4, column = 0)

RT60diff_label = ttk.Label(_mainframe, text = '')
RT60diff_label.grid(row = 5, column = 0)

ResonantFrequency_label = ttk.Label(_mainframe, text = '')
ResonantFrequency_label.grid(row = 6, column = 0)

# All buttons
selectBtn = ttk.Button(_mainframe, text='Select File', command=selectFile)
selectBtn.grid(row=1, column = 0, sticky = N, padx = 55)

lowRT60Btn = ttk.Button(_mainframe, state="disabled", text='Low RT60', command=lambda: (updateRT60(reverb.getRT60(200)), plt.clf(), reverb.dbplt(200), plt.show()))
lowRT60Btn.grid(row=7, column = 0, sticky = N, padx = 10)

midRT60Btn = ttk.Button(_mainframe, state="disabled", text='Mid RT60', command=lambda: (updateRT60(reverb.getRT60(1000)), plt.clf(), reverb.dbplt(1000), plt.show()))
midRT60Btn.grid(row=8, column = 0, sticky = N, padx = 10)

highRT60Btn = ttk.Button(_mainframe, state="disabled", text='High RT60', command=lambda: (updateRT60(reverb.getRT60(4000)), plt.clf(), reverb.dbplt(4000), plt.show()))
highRT60Btn.grid(row=9, column = 0, sticky = N, padx = 10)

combRT60Btn = ttk.Button(_mainframe, state="disabled", text='Combined RT60', command=lambda: (updateRT60(reverb.getCombinedRT60()), plt.clf(), reverb.dbplt(200), reverb.dbplt(1000), reverb.dbplt(4000), plt.show()))
combRT60Btn.grid(row=10, column = 0, sticky = N, padx = 10)

waveformBtn = ttk.Button(_mainframe, state="disabled", text='Waveform', command=lambda: (updateRT60(reverb.getCombinedRT60()), plt.clf(), reverb.waveformplt(), plt.show()))
waveformBtn.grid(row=11, column = 0, sticky = N, padx = 10)

spectBtn = ttk.Button(_mainframe, state="disabled", text='Spectrogram', command=lambda: (updateRT60(reverb.getCombinedRT60()), plt.clf(), reverb.specgram(), plt.show()))
spectBtn.grid(row=12, column = 0, sticky = N, padx = 10)

# Only run if main
if __name__ == "__main__":
    root.mainloop()
