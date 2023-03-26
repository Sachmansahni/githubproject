import random
import pywhatkit
import time
import pyttsx3
from playsound import playsound
pyobj=pyttsx3.init()
pyobj.setProperty("rate",180)


l = ["sachman", "ronit sachdeva", "rounak", "rounak raj", "rounak singh"]

gfeel = ["good", "happy", "well", "okay", "gud"]
bfeel = ["not", "bad", "worse", "worst"]

feelm = ["job", "boss", "breakup", "wife", "girlfriend", "gf", "health", "pain", "stress", "tension", "tensions",
         "problem", "problems", "money", "study", "accident", "low"]

print("hello this is alexa")
pyobj.say("hello this is ALEXA")
pyobj.runAndWait()
print("what can i do for u")
pyobj.say("what can i do for you?")
pyobj.runAndWait()

print("if you what to know about what i can do for u?")
pyobj.say("if you want to know about what i can do for you")
pyobj.runAndWait()
print()
time.sleep(1)
print("PRESS")
pyobj.say("press")
print("1 for yes")
print("2 for no")
pyobj.say("press 1 for yes and 2 for no")
pyobj.runAndWait()
print("or if you just wanna talk to me to make your mood light...")
print("simply say hello alexa or press 3")
pyobj.say("or if you just wanna talk to me to make your mood light")
pyobj.runAndWait()
pyobj.say("simply say hello alexa or press 3")
pyobj.runAndWait()

a = input()

if int(a) == 2:
    print("okay")
    pyobj.say("okay")
    pyobj.runAndWait()
    print("then why you called me?....HUH!!!")
    pyobj.say("then why you called me?...huh")
    pyobj.runAndWait()
    print("ajeeb aadmi hai")
    pyobj.say("ajeeb aadmi hai")
    pyobj.runAndWait()

elif int(a) == 3:
    print("hello there")
    pyobj.say("hello there")
    pyobj.runAndWait()
    print("nice to see you ")
    pyobj.say("nice to see you")
    pyobj.runAndWait()
    print("by the way who is there ???")
    pyobj.say("by the way who is there")
    pyobj.runAndWait()
    name = input()

    if name not in l:
        print("oh saw you here for the first time!never met you before")
        pyobj.say("oh saw you here for the first time!...never met you before")
        pyobj.runAndWait()

    else:
        if name == "rounak":
            print(" i found two identities with the given name in my memory!")
            print("please specify if it is rounak raj or rounak sahni ")
            pyobj.say("i found two identities with the given name in my memory! please specify if it is rounak raj or raunak sahni")
            pyobj.runAndWait()
            n2 = input()

    print("nice to see u ")
    print("how is the life going on ", name, "?")
    pyobj.say("nice to see you.how is the life going on",name)
    pyobj.runAndWait()
    lfeel = input().split()
    for feel in lfeel:
        if feel in gfeel:
            question = [1, 2, 3]
            print("oh touchwood...may god bless u always ")
            pyobj.say("oh touchwood...may god bless u always")
            pyobj.runAndWait()
            computer = random.choice(question)
            if question == 1:
                print("so,how is your family?")
                pyobj.say("so ,how is your family?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            elif question == 2:
                print("how is your job going on?")
                pyobj.say("how is your job going on?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            else:
                print("how was the day buddy?")
                pyobj.say("how was the day buddy?")
                pyobj.runAndWait()
                ans = input()
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()

            print("so do you want me to play a relaxing happy song for you?")
            pyobj.say("so do you want me to play a relaxing happy song for you?")
            pyobj.runAndWait()
            s = input()
            if s == "yes":
                print("do you want me to play this track on youtube or mp3")
                pyobj.say("do you want me to play this track on youtube or mp3?")
                pyobj.runAndWait()
                k = input("enter youtube or mp3")
                if k == "youtube":
                    pywhatkit.playonyt("sooraj ki baaho main")
                else:
                    playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")

            else:
                print("okay")
                pyobj.say("okay")
                pyobj.runAndWait()
            print("so do your want me to do anything else???")
            pyobj.say("so do you want me to do anything else?")
            pyobj.runAndWait()
            el = input()
            if el == "no":
                print("okay!!")
                print("going to sleep")
                print("DON'T DISTURB")
                pyobj.say("okay...going to sleep.don't disturb")
                pyobj.runAndWait()
            # else:   idhr neeche waala saara copy hoga :pehle neeche ka complete krke fir copymario
            else:
                print("\n Just ask..")
                print("play music,\n send whatsapp message,\n play a youtube video,\n search on google,\n play games..")

                pyobj.say("just ask..play music,send watsapp message,play a youtube video,search on google,play games")
                pyobj.runAndWait()
                print("press 1- for sending a whatsapp message")
                time.sleep(1)
                print("press 2- for youtube videos")
                time.sleep(1)
                print("press 3- for google search")
                time.sleep(1)
                print("press 4- for offline downlaoded music")
                time.sleep(1)
                print("press 5- for playing games")
                time.sleep(1)

                pyobj.say("please enter yur choice")
                pyobj.runAndWait()
                b = int(input("enter your choice"))

                if b == 1:
                    pyobj.say("please enter the correct details below")
                    pyobj.runAndWait()
                    num = input("please enter the number with country code:")
                    msg = input("please type the message to be sent:")
                    hour = int(input("please enter the scheduled hour:"))
                    minute = int(input("please enter the scheduled minute:"))
                    pyobj.say("please wait a second...")
                    pyobj.runAndWait()
                    print("please wait a second")
                    pywhatkit.sendwhatmsg(num, msg, hour, minute)

                elif b == 2:
                    pyobj.say("enter the video topic ")
                    pyobj.runAndWait()
                    topic = input("enter the video topic:")
                    pywhatkit.playonyt(topic)  # you can even add a url

                elif b == 3:
                    pyobj.say("please enter the topic to be searched")
                    pyobj.runAndWait()
                    search = input("please enter the topic to be searched")
                    pywhatkit.search(search)

                elif b == 4:
                    print("No internet!!!")
                    pyobj.say("no internet")
                    pyobj.runAndWait()
                    print("NO WORRIES")
                    pyobj.say("no worries")
                    pyobj.runAndWait()
                    print("alexa has the feature to play the predownloaded songs when you are offline")
                    pyobj.say("alexa has the feature to play the predownloaded songs when you are offline")
                    pyobj.runAndWait()

                    print("following is the list of music downloaded in your system")
                    print("1.bandeya re bandeya")
                    print("2.bewafa nikli haaye tu")
                    print("3.sooraj ki baaho mein")
                    print("4.pocket mai rocket")
                    print("5.ae bhai zra dekhke chlo")

                    c = int(input("enter the corresponding song number "))
                    if c == 1:
                        playsound("//Users//rudraksh//Downloads//new_128_05 - Simmba (2018) - Bandeya Rey Bandeya.mp3")
                    elif c == 2:
                        playsound("//Users//rudraksh//Downloads//Bewafa-Nikli-Hai-Tu_192(PaglaSongs).mp3")
                    elif c == 3:
                        playsound("//Users//rudraksh//Downloads//Sooraj Ki Baahon Mein - Zindagi Na Milegi Dobara 320 Kbps.mp3")
                    elif c == 4:
                        playsound("//Users//rudraksh//Downloads//Pocket Mein Rocket - Rocket Singh - Salesman Of The Year 128 Kbps.mp3")
                    elif c == 5:
                        playsound("//Users//rudraksh//Downloads//Ae Bhai Zara Dekh Ke Chalo - Mera Naam Joker 128 Kbps.mp3")



                elif b == 5:
                    print("WELCOME TO THE GAME PARK")
                    pyobj.say("welcome to the game park")
                    pyobj.runAndWait()
                    print()
                    print("which game do you want to play?")
                    print("press 1 for stone,paper,scissors")
                    print("press 2 for  guessing the number")
                    pyobj.say("which game do you want to play?  press 1 for stone paper scissors and press 2 for guessing the number games")
                    pyobj.runAndWait()
