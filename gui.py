import os.path
from tkinter import*
from tkinter import ttk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from convert import *
from reverb import *

reverb = Reverb()

def selectFile():
    filename = askopenfilename()
    if filename.endswith(".wav"):
        print(filename)
        print("Wav file accepted.")
        toMono(filename)
    elif filename.endswith(".mp3"):
        print(filename)
        print("File accepted.")
        mp3towav(filename)
        toMono("temp.wav")
    else:
        print("Please choose a .mp3 or .wav file.")
        return
    filename_label.config(text=f"Current file: {os.path.basename(filename)}")
    reverb.openFile("temp.wav")
    print(round(reverb.getTime(), 2), " seconds.")


root = Tk()
root.title('Sound Program')
root.geometry("300x200")

_mainframe = ttk.Frame(root, padding='5 5 5 5 ')
_mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S"))

canvas = ttk.Canvas(root)
canvas.pack()

selectBtn = ttk.Button(_mainframe, text='Select File', command=selectFile)
selectBtn.grid(row=1, column = 0, sticky = W, padx = 10)

lowRT60Btn = ttk.Button(_mainframe, text='Low RT60', command=lambda: reverb.dbplt(250))
lowRT60Btn.grid(row=3, column = 0, sticky = W, padx = 10)

midRT60Btn = ttk.Button(_mainframe, text='Mid RT60', command=lambda: reverb.dbplt(1000))
midRT60Btn.grid(row=4, column = 0, sticky = W, padx = 10)

highRT60Btn = ttk.Button(_mainframe, text='High RT60', command=lambda: reverb.dbplt(4000))
highRT60Btn.grid(row=5, column = 0, sticky = W, padx = 10)

combRT60Btn = ttk.Button(_mainframe, text='Select File', command=selectFile)
combRT60Btn.grid(row=1, column = 0, sticky = W, padx = 10)

waveformBtn = ttk.Button(_mainframe, text='Select File', command=selectFile)
waveformBtn.grid(row=1, column = 0, sticky = W, padx = 10)

SpectBtn = ttk.Button(_mainframe, text='Select File', command=selectFile)
SpectBtn.grid(row=1, column = 0, sticky = W, padx = 10)

fileFrame = ttk.Frame(root, relief='sunken')
fileFrame.grid(row = 2, column = 0, sticky=("E", "W", "S"))
fileFrame = ttk.LabelFrame(_mainframe, text = '')
filename_label = ttk.Label(_mainframe, text ='')
filename_label.grid(row = 2, column = 0)

root.mainloop()