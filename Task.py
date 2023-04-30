from speakai import say
import datetime


def Time():
    times = datetime.datetime.now().strftime("%H:%M %p")
    say(f"the time is {times}")


def Date():
    dates = datetime.date.today()
    say(f"it's {dates}")


def Day():
    days = datetime.datetime.now().strftime("%A")
    say(f"today is {days}")


def nowexit():
    l = ["Bye Sir. Have a nice day", "Good Bye. Have a nice day", "Take care!",
         "It'll be Nice To Meet You Again.", "See You Later"
         ]
    import random
    a = random.choices(l)
    say(a)
    exit()

def news():
    import requests
    import random
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "in",
        "apiKey": "a81acfa08a4d4e14adbc4e8958fa84ed"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        articles = response.json()["articles"]
        random_articles = random.sample(articles, 5)
        for i, article in enumerate(random_articles):
            a = article['title']
            a = a.replace("-", "by")
            say(a)
    else:
        say("Failed to retrieve news articles.")
def NonInputExectrion(quary):
    print(quary)
    if "exit" in quary:
        nowexit()
    elif "time" in quary:
        Time()
    elif "date" in quary:
        Date()
    elif "day" in quary:
        Day()
    elif "news" in quary:
        news()


def InputExectrion(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("what is", "").replace("who is", "").replace("tell me about", "").replace(
            "search for", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name, sentences=3)
        say(f"according to wikipedia {result}")
    elif "google" in tag:
        query = str(query).replace("google", "").replace("search for", "").replace("google for", "").replace("search",
              "").replace("google search", "")
        import pywhatkit
        say("Searching")
        pywhatkit.search(query)
    elif "youtube" in tag:
        query = str(query).replace("youtube", "").replace("youtube for", "").replace("youtube search", "")
        import pywhatkit
        say("Playing on youtube")
        pywhatkit.playonyt(query)
