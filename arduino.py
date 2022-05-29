from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound
def hello():
    root.destroy()
    import bot
def welso():
    playsound("song1.mp3")
root=Tk()
root.title("Arduino control")
photo =ImageTk.PhotoImage(file = "logo.jpg")
root.iconphoto(False, photo)
root.geometry("500x521")
root.maxsize(500,521)
root.minsize(500,521)
file="gif2.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))
gif_label =Label(root,image="")
gif_label.pack()
animation(count)
but1=Button(root,text="Start",padx=223,pady=10,bg="green",command=hello)
but1.pack()

welso()
root.mainloop()