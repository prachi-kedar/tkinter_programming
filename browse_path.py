from tkinter.filedialog import askdirectory
from tkinter import *
import os 
import shutil

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = askdirectory()
    folder_path.set(filename)
 


def browse_button2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_pathh
    filename = askdirectory()
    folder_pathh.set(filename)
    print(filename)


def move_files():
   src_path = folder_path
   dest_path = folder_pathh
   file_names = os.listdir(src_path)
   for file_name in file_names:
    shutil.move(os.path.join(src_path, file_name), dest_path)
   

root = Tk()

folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

folder_pathh = StringVar()
lbl2 = Label(master=root,textvariable=folder_pathh)
lbl2.grid(row=1, column=1)
button3 = Button(text="Browse1", command=browse_button2)
button3.grid(row=1, column=3)


b = Button(root, text="Move", command=move_files).grid(row=3, column=0,sticky=W+E+N+S, pady=4)
b1 = Button(root, text='Quit', command=root.quit).grid(row=3, column=1,sticky=W+E+N+S, pady=4) 
 

mainloop()
