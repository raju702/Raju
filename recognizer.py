import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = rec.listen(source)

try:
    text = rec.recognize_google(audio)
    print('You said: {}'.format(text))
except Exception as e:
    print("Error: {}".format(e))
