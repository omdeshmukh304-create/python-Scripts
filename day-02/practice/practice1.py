import requests

joke_url = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    joke = requests.get(url=joke_url)
    final_joke = joke.json()["setup"] + joke.json()["punchline"]
    return final_joke



final_joke = get_joke()
print(final_joke)
