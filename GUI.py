from tkinter import *
import GenerateCoverArt

root = Tk()

root.title("GenerateCoverArt")
root.geometry('320x200+0+0')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)

lbl = Label(root, text = "Generate an image based on the lyrics of your favorite song!")
lbl.grid()

titlePrompt = Label(root, text = "Enter the title of your song")
titlePrompt.grid(column=0, row=1)
title = Entry(root, width=20)
title.grid(column =0, row =2)

authorPrompt = Label(root, text = "Enter the author of your song")
authorPrompt.grid(column=0, row=3)
author = Entry(root, width=20)
author.grid(column =0, row =4)
 

def clicked():
    clean_author=''.join(letter for letter in author.get() if letter.isalnum())
    clean_title=''.join(letter for letter in title.get() if letter.isalnum())
    GenerateCoverArt.imageFromSong(clean_author, clean_title)
 
# button widget with red color text inside
btn = Button(root, text = "Generate Image" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=0, row=6)

root.mainloop()