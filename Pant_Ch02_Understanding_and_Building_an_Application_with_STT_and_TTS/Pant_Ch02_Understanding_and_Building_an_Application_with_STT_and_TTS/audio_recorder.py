import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

with open("recording.wav", "wb") as f:
    f.write(audio.get_wav_data())
