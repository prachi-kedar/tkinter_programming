import os
import shutil
from tkinter.filedialog import askdirectory
from tkinter import *

def src_button():
    global folder
    folder = askdirectory()
    folder_path.set(folder)
       
def dest_button():
    global folder1
    folder1 = askdirectory()
    folder_pathh.set(folder1)
    
def move_files():
   src_path = folder
   dest_path = folder1
   file_names = os.listdir(src_path)
   for file_name in file_names:
    shutil.move(os.path.join(src_path, file_name), os.path.join(dest_path, file_name))
   
root = Tk()

folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Source Folder", command=src_button)
button2.grid(row=0, column=3)

folder_pathh = StringVar()
lbl2 = Label(master=root,textvariable=folder_pathh)
lbl2.grid(row=1, column=1)
button3 = Button(text="Destination Folder", command=dest_button)
button3.grid(row=1, column=3)


b = Button(root, text="Move Files", command=move_files).grid(row=3, column=0,sticky=W+E+N+S, pady=4)
b1 = Button(root, text='Quit', command=root.quit).grid(row=3, column=1,sticky=W+E+N+S, pady=4) 
 
mainloop()
