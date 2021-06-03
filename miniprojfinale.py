from tkinter import *
from gtts import gTTS
from playsound import playsound
import random
import string
from tkinter import messagebox
import subprocess

accentext=""
filename=""
root = Tk()
root.geometry("1383x768")
root.configure(bg='#FFFFFF')
root.title("Text To Speech")


Msg = StringVar()

radioinput = IntVar()

frame1=LabelFrame(root, padx=522, pady=17, bg="#AE275F")
frame1.place(x=0, y=0)
Label(frame1, text = "Text To Speech", font = "arial 38 bold",bg="#AE275F" ,fg='#FFFFFF').pack()

Label(root,text ="Enter Text", font = 'arial 25 bold', fg="#AE275F", bg="#FFFFFF").place(x=446,y=110)

entry_field = Entry(root, textvariable = Msg ,width ='80')

entry_field.place(x=446,y=170)

def Text_to_speech():
    global filename
    path = r"F:\miniproj\ "
    filename = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 7))
    Message = entry_field.get()
    
    if len(Message)!=0:
        if len(accentext)!=0:
            speech = gTTS(text = Message, lang='en', tld=accentext)
            speech.save(path+str(filename)+".mp3")
            playsound(path+str(filename)+".mp3")
            print(filename)
        else:
            messagebox.showinfo("Alert", "Please select Accent")
            print("accent select")
    else:
        
        messagebox.showinfo("Alert","Please enter text!")
        print("notext")
        
    
    
def Exit():
    root.destroy()

def locate():
    subprocess.Popen(r'explorer /select,"F:\miniproj\ '+filename+r".mp3\"")
    
def Reset():
    Msg.set("")

def accent():
    global accentext
    val=str(radioinput.get())
    print(val)
    if int(val)==1:
        accentext="co.in"
        accentName="Indian"
    elif int(val)==2:
        accentext="com"
        accentName="American"
    elif int(val)==3:
        accentext="co.uk"
        accentName="British"

    accentLabel=Label(root, text=accentName+" accent selected", fg="#AE275F",bg="#FFFFFF", font="arial 19 bold")
    accentLabel.place(x=550, y=550)
    print(accentext)
    
    
Button(root, text = "Play", font = 'arial 15 bold' , command = Text_to_speech ,width = '6', bg='#AE275F', fg='#FFFFFF', activebackground='#faf0e6', activeforeground='#AE275F').place(x=470,y=220)

Button(root, font = 'arial 15 bold',text = 'Reset', width = '6' , command = Reset, bg="#faf0e6", fg="#AE275F", activeforeground="#faf0e6", activebackground="#AE275F").place(x=590 , y = 220)

Button(root, font = 'arial 15 bold',text = 'Locate', width = '6' , command = locate, bg = '#faf0e6', fg="#AE275F", activeforeground="#faf0e6", activebackground="#AE275F").place(x=710 , y = 220)

Button(root, font = 'arial 15 bold',text = 'Exit', width = '6' , command = Exit, bg="#faf0e6", fg="#AE275F", activeforeground="#faf0e6", activebackground="#AE275F").place(x=830 , y = 220)


can=Canvas(root, width=250, height=170, bg="#AE275F")
can.place(x=560, y=330)
Label(can, text="Accent",bg="#AE275F",fg="#FFFFFF", font="arial 19 bold").place(x=90, y=7)

R1 = Radiobutton(can, text="Indian", font="arial 15 bold",variable=radioinput,fg="#FFFFFF", bg="#AE275F",value=1, command=accent)
R1.place(x=12, y=45)

R2 = Radiobutton(can, text="American",font="arial 15 bold", variable=radioinput,fg="#FFFFFF",bg="#AE275F", value=2, command=accent)
R2.place(x=12, y=75)

R3 = Radiobutton(can, text="British", font="arial 15 bold", variable=radioinput,fg="#FFFFFF",bg="#AE275F", value=3, command=accent)
R3.place(x=12, y=105)

root.mainloop()
