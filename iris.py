import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech= sr.Recognizer()
greeting_dict= {'hello': 'hello', 'hi': 'hi'}
open_launch_dict= {'open': 'open', 'launch': 'launch'}
social_media_dict= {'facebook':'http://www.facebook.com', 'twitter':'http://www.twitter.com', 'instagram':'http://www.instagram.com'}

mp3_greeting_list= ['sounds/greet_hello.mp3', 'sounds/greet_hi.mp3']
mp3_launching_list= ['sounds/Okay.mp3', 'sounds/Launching.mp3', 'sounds/Sure.mp3']


def play_sound(mp3_list):
    mp3= random.choice(mp3_list)
    playsound(mp3)

def read_voice():
    voice_text= ''
    print("Listening ...")
    with sr.Microphone() as source:
        audio= speech.listen(source=source, timeout=10, phrase_time_limit=5)
    try:
        voice_text= speech.recognize_google(audio)
    except sr.UnknownValueError as uve:
        pass
    except sr.RequestError as re:
        print("network error")
    except sr.WaitTimeoutError as wte:
        pass
    return voice_text

def is_valid_notes(greeting_dict, voice_notes):
    for key, value in greeting_dict.items():
        #Hello Iris
        try:
            if value == voice_notes.split(' ')[0]:
                return True
                break
            elif key == voice_notes.split(' ')[1]:
                return True
                break
        except IndexError as ie:
            pass
    return False

if __name__=='__main__':
    playsound('sounds/intro.mp3')
    while True:
        voice_notes = read_voice().lower()
        print("Ivy: {}".format(voice_notes))
        if is_valid_notes(greeting_dict, voice_notes):
            print('In greeting ...')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_notes(open_launch_dict, voice_notes):
            print('In Launching ...')
            play_sound(mp3_launching_list)
            if(is_valid_notes(social_media_dict, voice_notes)):
                # Launch Facebook
                key= voice_notes.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\ {}'.format(voice_notes.replace('open ','').replace('launch ','')))
            continue
        elif 'bye' in voice_notes:
            speak_text("Bye poo. Have a good day")
            exit()
