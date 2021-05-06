import os
from tkinter import *
 
def file_counter():
    dir_path = e1.get()
    count = len([item for item in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, item))])
    myText.set(count)
    
master = Tk()
myText=StringVar()

Label(master, text="Enter Directory Name").grid(row=0, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)

result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e1.grid(row=0, column=1)


b = Button(master, text="Enter", command=file_counter).grid(row=0, column=2,sticky=W+E+N+S, pady=4)
b1 = Button(master, text='Quit', command=master.quit).grid(row=0, column=6,sticky=W+E+N+S, pady=4) 
 
mainloop()
 



