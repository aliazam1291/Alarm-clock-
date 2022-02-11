import datetime
import pyttsx3
from playsound import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def alarm():
    speak('please enter the time when you want me to rang alarm')
    time = input('enter time here in H:M:S')
    while True:
        Time_ac = datetime.datetime.now()
        now = Time_ac.strftime('%H:%M:%S')
        if now==time:
            speak('Time to wake up sir')
alarm()