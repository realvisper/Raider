import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        clear()  
        banner = f"""
░▒█░░▒█░▀█▀░▒█▄░▒█░▒█▀▀▀█░▒█▀▀▀░▒█▄░▒█░▒█▀▀▀█
░░▒█▒█░░▒█░░▒█▒█▒█░░▀▀▀▄▄░▒█▀▀▀░▒█▒█▒█░░▄▄▄▀▀
░░░▀▄▀░░▄█▄░▒█░░▀█░▒█▄▄▄█░▒█▄▄▄░▒█░░▀█░▒█▄▄▄█

  ╔════════════════════════════════════════════════╗
  ║                    Inahee                     ║
  ║                                                ║
  ║  1. Raid Menu        4. Other Menu             ║
  ║  2. Nuke Menu        5. Exit Program           ║
  ║  3. Webhook Menu                               ║
  ╚════════════════════════════════════════════════╝
"""
        print(banner)
        print("  Made By Vnox")
        choice = input("> ").strip()

        if choice == "1":
            raid_menu()
        elif choice == "2":
            nuke_menu()
        elif choice == "3":
            webhook_menu()
        elif choice == "4":
            other_menu()
        elif choice == "5":
            print("  Exit Program. Bye!")
            exit()
        else:
            print("  Invalid Choice")
            time.sleep(1)