#!/usr/bin/python
import aiml
import subprocess
import os
import sys
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import time
#Robot brain will be in here :)
k = aiml.Kernel()

# k.learn("aiml/star.aiml")
k.learn("aiml/first.aiml")
k.learn("aiml/bot_profile.aiml")
k.learn("aiml/ai.aiml")
k.learn("aiml/greetings.aiml")
k.learn("aiml/event.aiml")
k.learn("aiml/greeting.aiml")

# set a constant

k.setBotPredicate("age","3")
k.setBotPredicate("birthday","Nov. 23, 2018")
k.setBotPredicate("email","salonidarji3335@gmail.com")
k.setBotPredicate("emotions","as a robot I lack human emotions")
k.setBotPredicate("family","chat bot")
k.setBotPredicate("gender","female")
k.setBotPredicate("genus","AIML")
k.setBotPredicate("job","chat bot")
k.setBotPredicate("looklike","a computer")
k.setBotPredicate("master"," saloni maitry and krishna")
k.setBotPredicate("name"," 'KriSaMa' The ChatBot")
k.setBotPredicate("os","Windows")
i = "0"

print("Do You Want to Speak or Type? (Enter 1 for Speak And 2 for Type)")
choice = input("Enter 1 or 2: ")
while True:
    #print("choice="+choice)
    if choice == '1':
      r = sr.Recognizer()
      with sr.Microphone() as source:
        print("(Speak quit for exit)  User : ")
        time.sleep(3)
        print("listening...")
        audio = r.listen(source)
        

      try:
        req = r.recognize_google(audio)
        print("user: " + r.recognize_google(audio))
        userInput = req
      except sr.UnknownValueError:
        print("Google speech recognition could not understand audio please speak again..")
      except sr.RequestError as e:
        print("Could not Request Results from google speech recognition Service: {0}".format(e))
    else:
      userInput = input("(type quit for exit)  User : ") 

      
    if userInput == "quit":
      print("Good Bye , Have A Nice Day")
      sys.exit(0) 
    response = k.respond(userInput) 
    print ('KRISAMA: '+response+'\n')
    
    # texttospeech = gTTS(text=response , lang='en')
    # print("Please Wait")
    # fileName = "s" + i + ".mp3"
    # texttospeech.save(fileName)
    # playsound(fileName)
    # os.remove(fileName)
    # i = i + "1"
    

    # and as speech
   