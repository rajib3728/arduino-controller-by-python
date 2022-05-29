
import tkinter as tk
from tkinter import ttk ,filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import webbrowser
import serial
import time
import pandas as pd
import subprocess

def submit():
    if w.get()=="":
        messagebox.showinfo("Error","Please provide baudrate")
    else:
       k=w.get()
        
def ard():
    k=9600
    arduino = serial.Serial(port=clicked.get(), baudrate=k)
    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
    while True:
        num = 53
    
        write_read(num)
       #print(value)

def show():
    messagebox.showinfo("Code to upload",' // open arduino ide and write this code and upload')

    l2.config(text='''
    void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    int state = Serial.parseInt();
    if (state == 53) {
      digitalWrite(13, HIGH);
      delay(5000);
    }
    else
    {
      digitalWrite(13, LOW);
    }
  }
  delay(50);
}
    '''
    )
def ard2():
    k=9600
    arduino = serial.Serial(port=clicked.get(), baudrate=k)
    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
  
    num = 10
    write_read(num)

def copy1():
   df=pd.DataFrame(['''
void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    int state = Serial.parseInt();
    if (state == 53) {
      digitalWrite(13, HIGH);
      delay(5000);
    }
    else
    {
      digitalWrite(13, LOW);
    }
  }
  delay(50);
}
    '''])
   df.to_clipboard(index=False,header=False)
def openapp():
  subprocess.call("C:\\Program Files (x86)\\Arduino\\arduino.exe")
def helpp():
  webbrowser.open("help.html")
def clen():
  l2.config(text="")
def ard4():
    k=9600
    arduino = serial.Serial(port=clicked.get(), baudrate=k)
    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
  
    num = 10
    write_read(num)
    hello=arduino.readline()
    l2.config(text=hello)

root = tk.Tk()
root.geometry("1600x900")
root.title("Arduino control")
bg=ImageTk.PhotoImage(file="robo.jpg")
bglb=tk.Label(root,image=bg)
bglb.place(x=0,y=0,height=900,width=1600)
photo =ImageTk.PhotoImage(file = "logo.jpg")
root.iconphoto(False, photo)

start = tk.Button(root,text="code",bg="green",padx=25,pady=5,font=15,command=show)
start.place(x=20,y=40)

stop = tk.Button(root,text="copy",bg="red",padx=25,pady=5,font=15,command=copy1)
stop.place(x=120,y=40)
ard=tk.Button(root,text="click",bg="cyan",padx=25,pady=5,font=15,command=ard)
ard.place(x=220,y=40)

start2 = tk.Button(root,text="code",bg="green",padx=25,pady=5,font=15,command=show)
start2.place(x=20,y=100)

stop2 = tk.Button(root,text="copy",bg="red",padx=25,pady=5,font=15)
stop2.place(x=120,y=100)
ard2=tk.Button(root,text="click",bg="cyan",padx=25,pady=5,font=15,command=ard2)
ard2.place(x=220,y=100)

start3 = tk.Button(root,text="code",bg="green",padx=25,pady=5,font=15,command=show)
start3.place(x=20,y=160)

stop3 = tk.Button(root,text="copy",bg="red",padx=25,pady=5,font=15)
stop3.place(x=120,y=160)
ard3=tk.Button(root,text="click",bg="cyan",padx=25,pady=5,font=15,command=ard)
ard3.place(x=220,y=160)

start4 = tk.Button(root,text="code",bg="green",padx=25,pady=5,font=15,command=show)
start4.place(x=20,y=220)

stop4 = tk.Button(root,text="copy",bg="red",padx=25,pady=5,font=15)
stop4.place(x=120,y=220)
ard4=tk.Button(root,text="click",bg="cyan",padx=25,pady=5,font=15,command=ard4)
ard4.place(x=220,y=220)


but2=tk.Button(root,text="open arduino",bg="yellow",command=openapp)
but2.place(x=90,y=300)
but3=tk.Button(root,text="help?",command=helpp)
but3.place(x=1450,y=0)

cle=tk.Button(root,text="clean window",bg="yellow",command=clen)
cle.place(x=190,y=300)
# Dropdown menu options
options = [
    "COM3",
    "COM4",
    "COM5",
    "COM6",
    "COM7",
    "COM7",
    "COM9"
]
  
# datatype of menu text
clicked =tk. StringVar()
  
# initial menu text
clicked.set( "COM3" )
  
# Create Dropdown menu
drop = tk.OptionMenu( root , clicked ,*options )
drop.place(x=1200,y=690)
l2=tk.Label(root,text="select port",bg="yellow") 
l2.place(x=1207,y=670)
f1=tk.Frame(root,width=594,height=594,highlightcolor="black",highlightthickness=2)
f1.place(x=800,y=40)

l1=tk.Label(root,text="Enter baud rate",bg="yellow")
l1.place(x=820,y=670)
w=ttk.Entry(root,font=("Times New Roman",15,"bold"))
w.place(x=800,y=690,width=120)
btn1=tk.Button(root,text="Submit",command=submit,bg="black",fg="yellow")
btn1.place(x=920,y=690)

# write inside frame
l2=tk.Label(f1,text=None)
l2.place(x=160,y=60)

l3=tk.Label(f1,text="Your result",font=50,bg="cyan",padx=235,pady=20)
l3.place(x=10,y=0)
#root.wm_attributes('-transparentcolor', 'white')



root.mainloop()