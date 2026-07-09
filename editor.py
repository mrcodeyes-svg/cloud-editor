import tkinter as tk

#start root
root = tk.Tk()
#the main window
root.title('cloud editor')
root.geometry("500x500")

#add a button to tell the user where the editor is make it a button so the user can remove it
edit_lable = root.Button(root, text="editor")
#make it into a config
edit_lable.config(command= edit_lable.destroy)
root.mainloop()