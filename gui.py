from tkinter import*
from tkinter import ttk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from convert import*
from reverb import analyse


def selectFile():
    filename = askopenfilename(filetypes=(("wav File", "*.wav"), (("mp3 File", "*.mp3"))))
    #if filename.endswith(".mp3"):
     #   convertToWav(filename)
    convert1Chan(filename)
    print(filename)
    
def run():
    analyse()
    #analyse()

root = Tk()
root.title('Sound Program')
root.geometry("300x200")

_mainframe = ttk.Frame(root, padding='5 5 5 5 ')
_mainframe.grid(row=0, column=0, sticky=("E", "W", "N", "S"))

selectBtn = ttk.Button(_mainframe, text='Select File', command = selectFile)
selectBtn.grid(row=1, column = 0, sticky = W, pady = 75, padx = 100)

runBtn = ttk.Button(_mainframe, text='Analyse', command = run)
runBtn.grid(row=2, column = 0, sticky = W, pady = 0, padx = 100)

fileFrame = ttk.Frame(root, relief='sunken')
fileFrame.grid(row = 2, column = 0, sticky=("E", "W", "S"))

root.mainloop()