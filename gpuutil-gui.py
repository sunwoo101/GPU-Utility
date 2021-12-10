from tkinter import *
from tkinter.font import *
import subprocess
import os

password = ""

def cleanup(event=None):
    global password
    password = user_password_entry.get()
    popup.destroy()

def dynamic():
    global password
    os.system(f"echo {password} | sudo -S sudo pmset -a gpuswitch 2")
    gpu_mode_string.set("GPU Mode: Dynamic")

def dedicated():
    global password
    os.system(f"echo {password} | sudo -S sudo pmset -a gpuswitch 1")
    gpu_mode_string.set("GPU Mode: Dedicated")

def integrated():
    global password
    os.system(f"echo {password} | sudo -S sudo pmset -a gpuswitch 0")
    gpu_mode_string.set("GPU Mode: Integrated")

def button(row, column, text, command):
    button_frame = Frame(root, width=150, height=50)
    button_frame.grid_propagate(False)
    button_frame.grid(row=row, column=column)

    button = Button(button_frame, text=text, activeforeground="grey",
                    command=command, compound="left")
    button.grid(row=1, column=1, sticky="nsew")
    Grid.columnconfigure(button_frame, 1, weight=1)
    Grid.rowconfigure(button_frame, 1, weight=1)

# Enter password popup window #
popup = Tk()
popup.title("Enter password for user")
x_center = (popup.winfo_screenwidth()/2) - (200/2)
y_center = (popup.winfo_screenheight()/2) - (100/2)
popup.geometry(f"{200}x{100}+{int(x_center)}+{int(y_center)}")
popup.resizable(width=False, height=False)

# Label
user_password_label_string = StringVar()
user_password_label = Label(popup, textvariable=user_password_label_string)
user_password_label["font"] = Font(size=16)
user_password_label_string.set("User password:")
user_password_label.grid(row=1, column=1)

# Entry
user_password_entry_frame = Frame(popup, width=200, height=26)
user_password_entry_frame.grid_propagate(False)
user_password_entry_frame.grid(row=2, column=1)
Grid.rowconfigure(user_password_entry_frame, 2, weight=1)
Grid.columnconfigure(user_password_entry_frame, 1, weight=1)

user_password_entry = Entry(user_password_entry_frame)
user_password_entry.grid(row=2, column=1)
user_password_entry.configure(show="*")

# Confirm button
confirm_button_frame = Frame(popup, width=100, height=20)
confirm_button_frame.grid_propagate(False)
Grid.columnconfigure(confirm_button_frame, 1, weight=1)
Grid.rowconfigure(confirm_button_frame, 1, weight=1)
confirm_button_frame.grid(row=3, column=1, columnspan=2)

confirm_button = Button(confirm_button_frame,
                        text="Confirm", command=cleanup)
confirm_button.grid(row=1, column=1, sticky="nsew")

user_password_entry.bind("<Return>", cleanup)

popup.mainloop()

##################################################################

root = Tk()
root.title("GPU Utility")
width = 450
height = 80
x_center = (root.winfo_screenwidth()/2) - (width/2)
y_center = (root.winfo_screenheight()/2) - (height/2)
root.geometry(f"{width}x{height}+{int(x_center)}+{int(y_center)}")
root.resizable(width=False, height=False)

button(0, 0, "Dynamic", dynamic)
button(0, 1, "Dedicated", dedicated)
button(0, 2, "Integrated", integrated)

gpu_mode_string = StringVar()
gpu_mode_label = Label(
    root, textvariable=gpu_mode_string)
gpu_mode_label.grid(row=1, column=1)

root.mainloop()