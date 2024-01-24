from tkinter import *
from customtkinter import *
import GenerateCoverArt

root = CTk()

root.title("GenerateCoverArt")
root.geometry('350x250+0+0')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

set_appearance_mode("dark")

lbl = CTkLabel(master=root, text = "Generate an image based on the lyrics of your favorite song!")
lbl.grid()

titlePrompt = CTkLabel(root, text = "Enter the title of your song")
titlePrompt.grid(column=0, row=1)
title = CTkEntry(root)
title.grid(column =0, row =2)

authorPrompt = CTkLabel(root, text = "Enter the author of your song")
authorPrompt.grid(column=0, row=3)
author = CTkEntry(root)
author.grid(column =0, row =4)
 

def clicked():
    clean_author=''.join(letter for letter in author.get() if letter.isalnum())
    clean_title=''.join(letter for letter in title.get() if letter.isalnum())
    GenerateCoverArt.imageFromSong(clean_author, clean_title)
 
spacing = CTkLabel(root, text = "")
spacing.grid(column=0, row=5)
btn = CTkButton(master=root, text = "Generate Image", corner_radius=32, command=clicked)

btn.grid(column=0, row=6)

root.mainloop()