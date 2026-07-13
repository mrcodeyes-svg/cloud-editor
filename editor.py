import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import os
import time
import json

#start root
root = tk.Tk()
#the main window
root.title('cloud editor')
root.geometry("500x500")
#the folder and file vars
folder = ''
file = ''

#a label telling you which folder you are in
in_path = tk.Label(root, text="folder path: None")

#make a function to get the file or folder
def get_file(box = tk.Text, type= ""):
    global file, folder
    if type == 'file':
        #get the users file path
        file = filedialog.askopenfilename(title = "load a file")
        #if we got the file open it
        if file:
            in_path.config(text=f"file path: {file}")
            with open(file, 'r') as f:
                data = f.read()
                box.delete("1.0", tk.END)
                box.insert("1.0", data)
    #if it is folder then we get a folder dir
    elif type == 'folder':
        folder = filedialog.askdirectory(title="Select a Folder to Use")
        in_path.config(text=f"folder path: {folder}")
        
#make another function to save it
def save_file(path, box = tk.Text):
    global save
    #open the same file to write to it
    with open(path, 'w') as f:
        save.config(text=f"saving to {f}")
        f.write(box.get("1.0", tk.END).strip())
        save.config(text="save")

#make a function that will make a file
def make_file(folder2):
    global create, editor, file
    #check if there is a folder
    if folder2:
        path = os.path.join(folder2, simpledialog.askstring('input', 'what is your file name'))
        with open(path, 'w') as f:
            into_file = messagebox.askyesno("open", "do you want to open into your file")
            if into_file:
                #get the users file path
                file = path
                #if we got the file open it
                if file:
                    in_path.config(text=f"file path: {file}")
                    editor.delete("1.0", tk.END)
            f.write('')
    else:
        create.config(text="error: no folder opened")
        root.after(3000, lambda: create.config(text="create file"))

#make a function that opens a settings window
def open_settings():
    #make a new window
    seting = tk.Toplevel(root)
    seting.title('settings')
    seting.geometry("300x300")
    #the load button means load file
    load_f = tk.Button(seting, text='load file', command = lambda: get_file(editor, 'file'))
    #another load button means load folder
    load_fo = tk.Button(seting, text='load folder', command = lambda: get_file(editor, 'folder'))
    #the save button
    save = tk.Button(seting, text='save', command = lambda: save_file(file, editor))
    #a create button
    create = tk.Button(seting, text='create file', command = lambda: make_file(folder))
    #a delete window button
    delete_win = tk.Button(seting, text="\u2716", command = seting.destroy)
    #a check button to check auto save and add a settings.json
    try:
        with open('settings.json', 'r') as f:
            data = json.load(f)
            check = data['check']
    except Exception:
        #make the data
        data = {'check': False}
        #open it and write to it
        with open(settings.json, 'w') as f:
            json.dump(data, f, indent=4)
            check = False
    #the button
    auto_save = tk.Checkbutton(seting, text="auto save", variable=check)
    #pack them
    delete_win.pack(side=tk.TOP, anchor="e")
    load_f.pack()
    load_fo.pack()
    save.pack()
    create.pack()

#a button to launch settings
settings_open = tk.Button(root, text="settings", command = open_settings)
#add a button to tell the user where the editor is make it a button so the user can remove it
edit_lable = tk.Button(root, text="this is the editor \u2B07 \u2B07 \u2716")
#the editor
editor = tk.Text(root)
#make it into a config
edit_lable.config(command = edit_lable.destroy)
#pack them
settings_open.pack()
in_path.pack()
edit_lable.pack()
editor.pack()
#main loop
root.mainloop()
