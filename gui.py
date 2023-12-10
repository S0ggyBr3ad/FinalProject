import os.path
from tkinter import*
from tkinter import ttk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from convert import *
from reverb import *
def selectFile():
    filename = askopenfilename()
    print(filename) 
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
    filename_label.config(text = f"Current file: {os.path.basename(filename)}")
    analyse("temp.wav")


root = Tk()
root.title('Sound Program')
root.geometry("300x200")

_mainframe = ttk.Frame(root, padding='5 5 5 5 ')
_mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S"))

selectBtn = ttk.Button(_mainframe, text='Select File', command=selectFile)
selectBtn.grid(row=1, column = 0, sticky = W, padx = 10)

fileFrame = ttk.Frame(root, relief='sunken')
fileFrame.grid(row = 2, column = 0, sticky=("E", "W", "S"))
fileFrame = ttk.LabelFrame(_mainframe, text = '')
filename_label = ttk.Label(_mainframe, text ='')
filename_label.grid(row = 11, column = 0)

root.mainloop()