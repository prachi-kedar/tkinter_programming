import os
from tkinter import *
import shutil
 
def move_files():
   src_path = e1.get()
   dest_path = e2.get()
   file_names = os.listdir(src_path)
   for file_name in file_names:
    shutil.move(os.path.join(src_path, file_name), dest_path)
   
    
    
master = Tk()
myText=StringVar()

Label(master, text="Enter Source").grid(row=0, sticky=W)
Label(master, text="Enter Destination").grid(row=1, sticky=W)

e1 = Entry(master)
e1.grid(row=0, column=1)

e2 = Entry(master)
e2.grid(row=1, column=1)


b = Button(master, text="Move", command=move_files).grid(row=3, column=0,sticky=W+E+N+S, pady=4)
b1 = Button(master, text='Quit', command=master.quit).grid(row=3, column=1,sticky=W+E+N+S, pady=4) 
 
mainloop()
 



