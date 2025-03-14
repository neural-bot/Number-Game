# pip python package installer
# pyttsx3

import pyttsx3
import cowsay

text = "Thank you for joining with us"

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

cowsay.cow("See You Soon")