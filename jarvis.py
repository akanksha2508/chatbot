import os
import pyttsx3 as  p

p.speak("Welcome , how may I help you ")
a=input("Welcome , how may I help you ?")
a=a.lower()
b=("open" in a or "execute" in a or "run" in a or "launch" in a or "start" in a)
while True:
    #browser
    if (b) and ("chrome" in a or "web browser" in a or "browser" in a or "google" in a):
        os.system("chrome")
        p.speak("Opening chrome")
    #editor
    elif (b) and ("editor" in a or "notepad" in a or "atom" in a):
        if ("notepad" in a):
            os.system("notepad")
            p.speak("Launching notepad")
        else:
            os.system("start atom")
            p.speak("Launching atom")

    #windows player
    elif (b) and ("media player" in a or "windows media player" in a):
        os.system("wmplayer")
        p.speak("Launching Windows Media Player")
    #anydesk
    elif (b) and ("anydesk" in a ):
        os.system("anydesk")
        p.speak("Launching AnyDesk")
    #juypter notebook
    elif (b) and ("jupyter" in a or "jupyter notebook" in a):
        os.system("start jupyter notebook")
        p.speak("Launching jupyter Notebook")
    #vlc
    elif((b) and ("vlc" in a)):
        os.system("vlc")
        p.speak("starting a vlc")
    #calculator
    elif (b) and ("calculator" in a or "cal" in a or "calci" in a):
        os.system("calc")
        p.speak("Opening Calculator")
    #vm
    elif (b) and ("vm" in a or "virtual machine" in a):
        p.speak("Tell machine name")
        c=input("VM Name")
        os.system("virtualboxvm --startvm "+ c)
        p.speak("Launching virtual machine")
    #androidstudio
    elif (b) and ("android studio" in a):
        os.system("studio64.exe")
        p.speak("Launching Android Studio")
    #system configuration
    elif (("show" in a or "display" in a or "open" in a) and ("computer specific properties" in a or "computer specific configuration" in a)):
        os.system("systeminfo")
        p.speak("Displaying your System Configurations")
    #exit
    elif ("close" in a or "exit" in a):
        p.speak("Bye..we are closing now. Happy to help you")
        exit()
    else:
        p.speak("We don't support this")
