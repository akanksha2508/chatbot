import os
import pyttsx3 as  p

p.speak("Welcome , tell me your name")
d=input()
p.speak("Welcome"+d)

while True:
    p.speak("How may I help you ?")
    a=input("How may I help you ?")
    a=a.lower()
    b=("open" in a or "execute" in a or "run" in a or "launch" in a or "start" in a)
    #browser
    if (b) and ("chrome" in a or "web browser" in a or "browser" in a or "google" in a):
        p.speak("Opening chrome")
        os.system("chrome")

    #editor
    elif (b) and ("editor" in a or "notepad" in a or "atom" in a):
        if ("notepad" in a):
            p.speak("Launching notepad")
            os.system("notepad")

        else:
            p.speak("Launching atom")
            os.system("start atom")


    #windows player
    elif (b) and ("media player" in a or "windows media player" in a):
        p.speak("Launching Windows Media Player")
        os.system("wmplayer")

    #anydesk
    elif (b) and ("anydesk" in a ):
        p.speak("Launching AnyDesk")
        os.system("anydesk")

    #juypter notebook
    elif (b) and ("jupyter" in a or "jupyter notebook" in a):
        p.speak("Launching jupyter Notebook")
        os.system("start jupyter notebook")

    #vlc
    elif((b) and ("vlc" in a)):
        p.speak("starting a vlc")
        os.system("vlc")

    #calculator
    elif (b) and ("calculator" in a or "cal" in a or "calci" in a):
        p.speak("Opening Calculator")
        os.system("calc")

    #vm
    elif (b) and ("vm" in a or "virtual machine" in a):
        p.speak("Tell machine name")
        c=input("VM Name")
        p.speak("Launching virtual machine")
        os.system("virtualboxvm --startvm "+ c)

    #androidstudio
    elif (b) and ("android studio" in a):
        p.speak("Launching Android Studio")
        os.system("studio64.exe")

    #system configuration
    elif (("show" in a or "display" in a or "open" in a) and ("computer specific properties" in a or "computer specific configuration" in a)):
        p.speak("Displaying your System Configurations")
        os.system("systeminfo")
    elif "youtube" in a:

        p.speak("What are you looking for?")
        print("What are you looking for?")
        q=input()
        q=q.lower()
        p.speak("Okay! opening {} in YouTube".format(q))
        try:
            os.system("chrome https://www.youtube.com/results?search_query={}".format(q))
        except:
            print("Error...try again")

    #exit
elif ("close" in a or "exit" in a or 'bye' in a):
        p.speak("Bye..we are closing now. Happy to help you")
        exit()
    else:
        p.speak("We don't support this")
