import pyttsx3


def say(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty("rate", 200)
    print(f"A.I : {text}")
    engine.say(text=text)
    engine.runAndWait()
    print("     ")


def Newvoices():
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        engine.say("Hello World!")
        engine.runAndWait()
        engine.stop()
