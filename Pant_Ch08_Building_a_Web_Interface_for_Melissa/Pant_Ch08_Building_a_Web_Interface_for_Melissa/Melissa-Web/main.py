import os
import sys
import time

import yaml
import pyaudio
import speech_recognition as sr

from brain import brain
from GreyMatter import play_music
from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
music_path = profile_data['music_path']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password']
access_token = profile_data['twitter']['access_token']
access_token_secret = profile_data['twitter']['access_token_secret']
consumer_key = profile_data['twitter']['consumer_key']
consumer_secret = profile_data['twitter']['consumer_secret']

voice_file = os.getcwd() + '/uploads/' + sys.argv[1]

def main(voice_file):
    r = sr.Recognizer()
    with sr.WavFile(voice_file) as source:
        audio = r.record(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Melissa thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Melissa could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    play_music.mp3gen(music_path)
    brain(name, speech_text, music_path, city_name, city_code, proxy_username, proxy_password)

main(voice_file)
