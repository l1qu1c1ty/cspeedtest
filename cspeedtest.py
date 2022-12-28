# Python program to test
# internet speed

import os
import speedtest
from pyfiglet import Figlet
from colorama import Fore

while True:
    f = Figlet()
    print(Fore.YELLOW,end="")
    print(f.renderText("SPEEDTEST"))

    print(Fore.GREEN,end="")
    option = input('''What speed do you want to test

    ------------------
    1) Download Speed
    2) Upload Speed
    3) Ping
    4) All (Download + Upload + Ping)
    5) Exit
    -----------------
Your Choice:''')

    print(Fore.LIGHTBLUE_EX,end="")

    st = speedtest.Speedtest()

    if option == "1":
        print("Download Speed:",end="")
        print(int(st.download()),"byte")
        input("Press Any Key...")
        print("\033[H\033[J", end="")

    elif option == "2":
        print("Upload Speed:",end="")
        print(int(st.upload()),"byte")
        input("Press Any Key...")
        print("\033[H\033[J", end="")

    elif option == "3":
        servernames = []
        st.get_servers(servernames)
        print("Ping:",end="")
        print(st.results.ping,"ms")
        input("Press Any Key...")
        print("\033[H\033[J", end="")

    elif option == "4":
        print("-"*35)
        print("Download Speed\t: ",end="")
        print(int(st.download())," byte")
        print("Upload Speed\t: ",end="")
        print(int(st.upload()),"  byte")
        servernames = []
        st.get_servers(servernames)
        print("Ping        \t: ",end="")
        print(st.results.ping,"   ms")
        print("-"*35)
        input("Press Any Key...")
        print("\033[H\033[J", end="")

    elif option == "q" or option == "5":
        print("\033[H\033[J", end="")
        break

    else:
        print(Fore.RED)
        print("Please enter the correct choice!")
        input("Press Any key...")
        print("\033[H\033[J", end="")


print(Fore.WHITE)