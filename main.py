import pyttsx3
import speech_recognition as sr
from vosk import Model,KaldiRecognizer
import pyaudio
import random

model = Model(r"vosk-model-small-en-us-0.15") #downloaded files
recognizer = KaldiRecognizer(model,16000)
wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices',voices[0].id)
mic = pyaudio.PyAudio()
voice = ''
badWords = ['fuck','ho','bitch']
greeting = ['hi','hello','hey']
goodWords = ['good morning','good evening','good night']
ending = ['go to sleep ','sleep','go to bed','Have nice day','close','end']
feelings = ['fine','realy sad','vary happy','too angry','vary vary good','truble','too bad','too bored']

def Speak (audio):
    wel.say(audio)
    wel.runAndWait()

def TakeCommends ():
    voice=''
    print('Recoding .....')
    stream =mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=32000)
    stream.start_stream()
    while True :
        data = stream.read(32000)
        if recognizer.AcceptWaveform(data) :
            text = recognizer.Result()
            voice = text[14:-3]
            print(voice)
            if  voice in badWords :
                Speak('I am ganna trying over')
            if voice in greeting :
                Speak(greeting[random.randrange(0,3)])
            if voice in goodWords  :
                Speak('')
            if voice in greeting:
                replaying = 'I am {0}. how about you sir'
                Speak(replaying.format(feelings[random.randrange(0,9)]))
            if voice in ending :
                Speak('Have nice day')
                return False
            else:
                return True

Speak('How can I help You  sir ..?')
while TakeCommends():
    TakeCommends()
