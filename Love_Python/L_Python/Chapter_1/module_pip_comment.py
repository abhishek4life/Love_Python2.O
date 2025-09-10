import pyjokes

joke = pyjokes.get_joke()
print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()