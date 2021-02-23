from pathlib import Path
import tkinter as tk
import main
import os


window = tk.Tk()
window.title("Player")
window.geometry("600x400")

link_var = tk.StringVar()
path_var = tk.StringVar()
path = r"C:\Users\tvten\PycharmProjects\vid download\Music"
my_path = Path(r"C:\Users\tvten\PycharmProjects\vid download")


def save():
    global path
    path = Path(path_var.get())

    path_edit_label.destroy()
    path_edit_entry.destroy()
    path_edit_button.destroy()

    if path.is_dir():
        pass
    else:
        os.mkdir(path)


path_edit_label = tk.Label(window, text="Enter the new path ")
path_edit_entry = tk.Entry(window, textvariable=path_var)
path_edit_button = tk.Button(window, text="Save", command=save)


def get_link():
    link = link_var.get()
    print(link)
    mp = tkvar.get()
    main.download(link, mp)


def edit():
    path_edit_label.grid(row=3, column=0)
    path_edit_entry.grid(row=3, column=1)
    path_edit_button.grid(row=3, column=2)


link_label = tk.Label(window, text="Enter the link of the playlist ").grid(row=0, column=0)
link_entry = tk.Entry(window, textvariable=link_var).grid(row=0, column=1)

check_button = tk.Button(window, text="Download", command=get_link).grid(row=0, column=2)
edit_path = tk.Button(window, text="Edit Path", command=edit).grid(row=2, column=0)

choices = {"mp3", "mp4"}
tkvar = tk.StringVar(window)
tkvar.set("        ")

mp_label = tk.Label(window, text="Choose how you want the videos to be saved ").grid(row=1, column=0)
popupmenu = tk.OptionMenu(window, tkvar, *choices).grid(row=1, column=1)


def change_dropdown(*args):
    print(tkvar.get())


tkvar.trace('w', change_dropdown)

window.mainloop()