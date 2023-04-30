import speech_recognition as sr


def Listen():
    quarry = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        quarry = r.recognize_google(audio, language="en-in")
        print(f"You Said : {quarry}")
    except:
        pass

    quarys = str(quarry)
    return quarys.lower()
