from typing import Text
from gtts import gTTS
from playsound import playsound
from tkinter import Tk, Label, StringVar, Entry, Button

root = Tk()
root.geometry("400x400")
root.title("Text to Speech")
root.config(bg="white")

Label(root, text="Text to Speech", bg="white smoke").pack()
Label(root, text="Enter text:", bg="white smoke").place(x=20, y=60)

Msg = StringVar()

input_field = Entry(root, textvariable=Msg, width="40")
input_field.place(x=20, y=100)


def tts():
    message = input_field.get()
    speech = gTTS(text=message)
    speech.save("speech.mp3")
    playsound("speech.mp3")

def Exit():
    root.destroy()

def Reset():
    Msg.set("")


Button(root, text="Play", command=tts, width=3).place(x=20, y=140)
Button(root, text="Exit", command=Exit, width=3).place(x=80, y=140)
Button(root, text="Reset", command=Reset, width=3).place(x=140, y=140)


root.mainloop()
