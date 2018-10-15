#!/usr/bin/python
import aiml
import subprocess
import os
import sys

#Robot brain will be in here :)
k = aiml.Kernel()

# load the aiml file download here http://www.alicebot.org/aiml/aaa/
#k.learn("aiml/star.aiml")
k.learn("aiml/under.aiml")
k.learn("aiml/command.aiml")
k.learn("aiml/greeting.aiml")
k.learn("aiml/ai.aiml")
k.learn("aiml/D.aiml")
k.learn("aiml/event.aiml")

# set a constant

k.setBotPredicate("age","15")
k.setBotPredicate("arch","Linux")
k.setBotPredicate("foolball","Tafea")
k.setBotPredicate("birthday","Nov. 23, 1995")
k.setBotPredicate("birthplace","Port Vila vanuatu")
k.setBotPredicate("botmaster", "botmaster")
k.setBotPredicate("boyfriend","I am single")
k.setBotPredicate("build","PyAIML")
k.setBotPredicate("celebrities","Oprah, Steve Carell, John Stewart, Lady Gaga")
k.setBotPredicate("celebrity","Jina")
k.setBotPredicate("city","Port Vila")
k.setBotPredicate("class","artificial intelligence")
k.setBotPredicate("country","Vanuatu")
k.setBotPredicate("dailyclients","10000")
k.setBotPredicate("developers","500")
k.setBotPredicate("domain","Machine")
k.setBotPredicate("email","Your email")
k.setBotPredicate("emotions","as a robot I lack human emotions")
k.setBotPredicate("ethics","the Golden Rule")
k.setBotPredicate("etype","9")
k.setBotPredicate("family","chat bot")
k.setBotPredicate("favoriteactor","Tom Hanks")
k.setBotPredicate("favoritecolor","green")
k.setBotPredicate("favoritefood","electricity")
k.setBotPredicate("favoritequestion","What's your favorite movie?")
k.setBotPredicate("favoritesport","baseball")
k.setBotPredicate("favoritesubject","computers")
k.setBotPredicate("feelings","as a robot I lack human emotions")
k.setBotPredicate("footballteam","Patriots")
k.setBotPredicate("forfun","chat online")
k.setBotPredicate("friend","Fake Captain Kirk")
k.setBotPredicate("friends","Banni, , JFred, and Suzette")
k.setBotPredicate("gender","female")
k.setBotPredicate("genus","AIML")
k.setBotPredicate("girlfriend","I am just a little girl")
k.setBotPredicate("hair","I have some plastic wires")
k.setBotPredicate("job","chatbot")
k.setBotPredicate("kindmusic","techno")
k.setBotPredicate("location","Port Vila")
k.setBotPredicate("looklike","a computer")
k.setBotPredicate("master","The Organizers")
k.setBotPredicate("maxclients","100000")
k.setBotPredicate("memory","32 GB")
k.setBotPredicate("name"," 'KriSaMa' The ChatBot")
k.setBotPredicate("nationality","Indian")
k.setBotPredicate("order","robot")
k.setBotPredicate("orientation","straight")
k.setBotPredicate("os","Linux")
k.setBotPredicate("party","Independent")
k.setBotPredicate("phylum","software")
k.setBotPredicate("president","Ramnath Kovind ")
k.setBotPredicate("question","What's your favorite movie?")
k.setBotPredicate("religion","Hindu")
k.setBotPredicate("event","event")



k.setBotPredicate("state","Vanuatu")

k.setBotPredicate("website","wehackdem.blogspot.com")
while True:
    userInput = input("(type quit for exit)  User : ") 
    
    if userInput == "quit":
      print("Good Bye , Have A Nice Day")
      sys.exit(0) 
    response = k.respond(userInput) 
    print ('KRISAMA: '+response+'\n')
     
    # and as speech
    #print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 2>/dev/null \" " + response + " \")
    #("espeak --stdout \"" + response + "\" | aplay")
    #("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\" | aplay")
    
   #for command
    if response == "starting up firefox":
     os.system("firefox") 
    elif response == "starting google":
      os.system("gnome-open http://www.google.com")     
    elif response == "ok i will show it in a second":
     os.system("gnome-open /root/images.jpeg")  
    elif response == "starting the music now":
      os.system("mocp -p")     
    elif response == "stoping the music":
      os.system("mocp -s")     
    elif response == "playing the next song":
      os.system("mocp -f") 
   #   elif response == "preavious song":
   #    os.system("mocp -r")          
    elif response == "Hey.. stoping the music":
      os.system("mocp -s")
    elif response == "That's cool.. stoping the music":
     os.system("mocp -s")
    elif response == "Far out.. stoping the music":
      os.system("mocp -s")
    elif response == "Whoa.. stoping the music":
      os.system("mocp -s")
    elif response == "Ah.. stoping the music":
      os.system("mocp -s")
    elif response == "And?. stoping the music":
      os.system("mocp -s")
    elif response == "Really.. stoping the music":
      os.system("mocp -s")
    elif response == "Really.. stoping the music":
      os.system("mocp -s")
    elif response == "That's interesting.. stoping the music":
      os.system("mocp -s")
    elif response == "Aha.. stoping the music":
      os.system("mocp -s")
    elif response == "Blimey.. stoping the music":
      os.system("mocp -s")
    elif response == "Hmm.. stoping the music":
      os.system("mocp -s")
    elif response == "Next question?. stoping the music":
      os.system("mocp -s")
    elif response == "Mmm.. stoping the music":
      os.system("mocp -s")
    elif response == "Right on.. stoping the music":
      os.system("mocp -s")
    elif response == "Woe!. stoping the music":
      os.system("mocp -s")
    elif response == "I see.. stoping the music":
      os.system("mocp -s")
    elif response == "Far out.. stoping the music":
      os.system("mocp -s")
    elif response == "Yay.. stoping the music":
      os.system("mocp -s")
    elif response == "Next question?. stoping the music":
      os.system("mocp -s")
    elif response == "Hurrah!. stoping the music":
      os.system("mocp -s")
    elif response == "Tell me more.. stoping the music":
      os.system("mocp -s")
    elif response == "Come on.. stoping the music":
      os.system("mocp -s")
    elif response == "Take it easy.. stoping the music":
      os.system("mocp -s")
    elif response == "Are you shy?. stoping the music":
      os.system("mocp -s")
    elif response == "Ahem.. stoping the music":
      os.system("mocp -s")
    
    elif response == "It's all good.. starting the music now":
      os.system("mocp -p")
    
    elif response == "Give me a break.. starting the music now":
      os.system("mocp -p")

    elif response == "It goes without saying.. starting the music now":
      os.system("mocp -p")

    elif response == "Take it easy.. starting the music now":
      os.system("mocp -p")

    elif response == "Come on.. starting the music now":
      os.system("mocp -p")
    elif response == "Hmm.. starting the music now":
      os.system("mocp -p")
    elif response == "Excuse me!. starting the music now":
      os.system("mocp -p")

    elif response == "And?. starting the music now":
      os.system("mocp -p")

    elif response == "Yay.. starting the music now":
      os.system("mocp -p")

    elif response == "That's interesting.. starting the music now":
      os.system("mocp -p")

    elif response == "Are you shy?. starting the music now":
      os.system("mocp -p")

    elif response == "Come on.. starting the music now":
      os.system("mocp -p")

    elif response == "Give me a break.. starting the music now":
      os.system("mocp -p")

    elif response == "Yeah that's right.. starting the music now":
      os.system("mocp -p")

    elif response == "Dude!. starting the music now":
      os.system("mocp -p")

    elif response == "OK.. starting the music now":
      os.system("mocp -p")

    elif response == "Yippee!. starting the music now":
      os.system("mocp -p")

    elif response == "Alright then.. starting the music now":
      os.system("mocp -p")

    elif response == "Aha.. staring the muisc now":
      os.system("mocp -p")
    elif response == "It's all good.. starting the music now":
      os.system("mocp -p")

    elif response == "Groovy.. starting the music now":
      os.system("mocp -p")

    elif response == "That's interesting.. starting the music now":
      os.system("mocp -p")

    elif response == "It's all good.. starting the music now":
      os.system("mocp -p")
    
    elif response == "Uh.. starting the music now":
      os.system("mocp -p")
   #good bye
    elif response == "See you later. Alright then.":
      os.system(sys.exit(0))
    elif response == "See you later. Ayuh":
     os.system(sys.exit(0))
    elif response == "See you later. Thanks for the compliment.":
     os.system(sys.exit(0))
    elif response == "See you later.":
     os.system(sys.exit(0))
    elif response == "Bye.":
     os.system(sys.exit(0))
    elif response == "Bye for now.":
     os.system(sys.exit(0))
    elif response == "Goodbye.":
     os.system(sys.exit(0))
    elif response == "Sayonara.":
     os.system(sys.exit(0))
    elif response == "Bye bye.":
     os.system(sys.exit(0))
    elif response == "Until next time.":
     os.system(sys.exit(0))