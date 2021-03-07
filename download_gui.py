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


def save():
    global path
    path = Path(path_var.get())
    path = (r'%s' % path)

    path_edit_label.destroy()
    path_edit_entry.destroy()
    path_edit_button.destroy()

    if not os.path.exists(path):
        os.mkdir(path)


path_edit_label = tk.Label(window, text="Enter the new path ")
path_edit_entry = tk.Entry(window, textvariable=path_var)
path_edit_button = tk.Button(window, text="Save", command=save)


def get_link():
    link = link_var.get()
    print(link)
    mp = tkvar_mp.get()
    link_type = tkvar_link.get()

    if link_type == "video":
        main.download_vid(link, path)
        if mp == "mp3":
            main.convert(path)
    else:
        main.download(link, path)
        if mp == "mp3":
            main.convert(path)


def edit():
    path_edit_label.grid(row=3, column=0)
    path_edit_entry.grid(row=3, column=1)
    path_edit_button.grid(row=3, column=2)


link_label = tk.Label(window, text="Enter the link of the playlist or the video ").grid(row=0, column=0)
link_entry = tk.Entry(window, textvariable=link_var).grid(row=0, column=1)

choices_link = {"video", "playlist"}
tkvar_link = tk.StringVar(window)
tkvar_link.set("        ")


def link_dropdown(*args):
    tkvar_link.get()


check_button = tk.Button(window, text="Download", command=get_link).grid(row=2, column=0)
edit_path = tk.Button(window, text="Edit Path", command=edit).grid(row=2, column=1)
popupmenu_link = tk.OptionMenu(window, tkvar_link, *choices_link).grid(row=0, column=2)
tkvar_link.trace('w', link_dropdown)

choices_mp = {"mp3", "mp4"}
tkvar_mp = tk.StringVar(window)
tkvar_mp.set("        ")

mp_label = tk.Label(window, text="Chose how you want the videos to be saved ").grid(row=1, column=0)
popupmenu_mp = tk.OptionMenu(window, tkvar_mp, *choices_mp).grid(row=1, column=1)


def change_dropdown(*args):
    tkvar_mp.get()


tkvar_mp.trace('w', change_dropdown)

window.mainloop()