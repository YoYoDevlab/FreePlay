
from tkinter import *
import winsound
import os
import requests
import shutil

def toPlay():
	try:
		data = entry.get()
		download = data
		r = requests.get(download)
		filename = r.url[download.rfind("/")+1:]
		with open(filename, "wb") as f:
			for chunk in r.iter_content(chunk_size=8192):
				if chunk:
					f.write(chunk)
		winsound.PlaySound(filename, winsound.SND_ASYNC)
	except:
		error = Label(text="No link found!", foreground="#ff0000").pack()

def filePlay():
	try:
		data = entry2.get()
		shutil.copyfile(data, "copiedFile.wav")
		winsound.PlaySound("copiedFile.wav", winsound.SND_ASYNC)
	except FileNotFoundError:
		FNF.pack()
	else:
		FNF.forget()

def pause():
	winsound.PlaySound("quiet.wav", winsound.SND_ASYNC)

def fromLink():
	label2.pack()
	entry.pack()
	btn.pack()
	pausebtn.pack()
	label4.forget()
	entry2.forget()
	btn2.forget()
	pausebtn1.forget()

def fromFile():
	label4.pack()
	entry2.pack()
	btn2.pack()
	pausebtn1.pack()
	label2.forget()
	entry.forget()
	btn.forget()
	pausebtn.forget()

root = Tk()

root.title("FreePlay")
root.iconbitmap("favicon.ico")
root.geometry("500x200")

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Play from...", menu=subMenu)
subMenu.add_cascade(label="Play from link", command=fromLink)
subMenu.add_cascade(label="Play from file", command=fromFile)

label = Label(text="Freeplay", width=10)
label.pack()

label2 = Label(text="Enter a .wav download link to begin.")

entry = Entry(root, borderwidth=2)

btn = Button(text="Play", width=4, height=1, command=toPlay)

pausebtn = Button(text="Stop", command=pause)

label4 = Label(text="Enter the file path to a .wav file.")

entry2 = Entry(root, borderwidth=2)

btn2 = Button(text="Play", width=4, height=1, command=filePlay)

pausebtn1 = Button(text="Stop", command=pause)

FNF = Label(text="File not found!", foreground="#ff0000")

label2.pack()
entry.pack()
btn.pack()
pausebtn.pack()

root.mainloop()