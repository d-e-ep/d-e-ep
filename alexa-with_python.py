import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('i am your alexa')
engine.say('what can i do for you')
engine.runAndWait()


try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
except:
    pass
  return command

def run_alexa():
    command = take_command()
    print(command)
    if 'paly' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    else'time' in command:
        time = datetime.datetime.now().strftime('%i:%M %p')
        print(time)
        talk('current time is'+ time)
                                                
            
run_alexa()
