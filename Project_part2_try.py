                             #GUI Interface


from tkinter import *
from PIL import Image , ImageTk
import Project_part4_try
import speech_recognition as sr


root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.minsize(700,600)         #minsize = (Width,Height)

root.maxsize(8000,8000)        #maxsize = (Width,Height)
root.size


root.config(bg="#6f8FAF")



#ask,send,delete functions

def ask ():
    user_val = Project_part4_try.convert_speech_to_text()
    bot_val  = Project_part4_try.handle_user_request(user_val)
    text.insert(END , "User--->"+user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT--->"+str(bot_val)+"\n")
    if bot_val == "Ok mam. Have a good day!" :
        root.destroy()

def send ():
    send = entry.get()
    bot = Project_part4_try.handle_user_request(send)
    text.insert(END , "User--->"+ send+"\n")
    if bot != None:
        text.insert(END , "BOT--->"+str(bot)+"\n")
    if bot == "Ok mam. Have a good day!" :
        root.destroy()

def del_text ():
    text.delete("1.0", "end")

#Frame

frame = LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label

text_label = Label(frame,text="Gracia Assistant",font=("comic Sans ms",14,"bold"))
text_label.grid(row=0,column=0,padx=20,pady=10)

#image

image=ImageTk.PhotoImage(Image.open("D:/Gracia_Assistant.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row = 1, column = 0 , pady = 20)

#adding a text widget

text = Text(root, font=('courier 10 bold'), bg ="#356696")
text.grid(row=2,column=0)
text.place(x=70,y=375,width=375,height=100)

#entry widget

entry = Entry(root,justify=CENTER)
entry.place(x=70,y=500,width=370,height=30)

#button 1

Button1 = Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)

#button 2

Button2 = Button(root,text="SEND",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=400,y=575)

#button 3
Button3 = Button(root,text="DELETE",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=225,y=575)

root.mainloop()


                    #Text_to_Speech Recognizition

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate','rate-70')

    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()





