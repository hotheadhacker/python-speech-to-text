import speech_recognition as sr
print(sr.__version__)
#setting class
r = sr.Recognizer()
#using recog. engine
# r.recognize_google()

#audio source
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

# print(r.recognize_google(audio))
txt = r.recognize_google(audio)
print(txt)

#saving data into a file
f = open("demofile2.txt", "a")
f.write(txt)
f.close()