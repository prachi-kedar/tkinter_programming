import time
import tkinter as tk
import tkinter.ttk as ttk


tuple_1 = tuple(range(1, 25))
brt = len(tuple_1)


def progress_bar_func():
    global num

    num = 1
    root.after(500, update_progress_bar)

def update_progress_bar():
    global num

    if num <= brt:
        percentage = round(num/brt*100)  # Calculate percentage.
        print(num, percentage)
        progressBar['value'] = num
        style.configure('text.Horizontal.TProgressbar',
                        text='{:g} %'.format(percentage))
        num += 1
        if num > brt:
            print('Done')
        else:
            root.after(500, update_progress_bar)


root = tk.Tk()
root.geometry("300x300")

style = ttk.Style(root)
style.layout('text.Horizontal.TProgressbar',
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('Horizontal.Progressbar.label', {'sticky': ''})])
              # , lightcolor=None, bordercolo=None, darkcolor=None
style.configure('text.Horizontal.TProgressbar', text='0 %')

progressBar = ttk.Progressbar(root, style='text.Horizontal.TProgressbar', length=200,
                              maximum=brt, value=0)
progressBar.pack()

progress_button = tk.Button(root, text="start", command=progress_bar_func)
progress_button.pack()

root.mainloop()
