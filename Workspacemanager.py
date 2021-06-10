import tkinter as tk
from tkinter import filedialog,scrolledtext
import os
import subprocess, sys
apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split(",")
        apps = [x for x in tempapps if x.strip()]


def addapp():
    for widgets in frame.winfo_children():
        widgets.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",   filetypes=(("executables","*.exe"),("all", "*.*")) )
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, bg="gray",text=app)
        label.pack()

def runapps():
    for app in apps:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, app])


root = tk.Tk()
canvas = tk.Canvas(root, height=700, width= 700, bg="#242424")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8 , relheight = 0.8, relx=0.1, rely=0.1)

openapp = tk.Button(root, text="openfile", padx =10,pady=5, bg="#242424",fg="white" ,command= addapp)
openapp.pack()

runapp = tk.Button(root, text="run", padx =10,pady=5, bg="#242424",fg="white", command=runapps)
runapp.pack()
for app in apps:
    label = tk.Label( frame, text =app )
    label.pack()


root.mainloop()
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")

