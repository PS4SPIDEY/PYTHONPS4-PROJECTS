import pyttsx3 as reader

while True:
    friend = reader.init()
    speech = input("Enter your value:-")

    friend.say(speech)
    friend.runAndWait()
