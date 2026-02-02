from player import Player
from utils import load_game, save_game, sprint, inp, cls
from player import Player
from story import show_intro

def main():
    sprint(r"""
/$$$$$$$$ /$$                       /$$   /$$           /$$           /$$         /$$               
|__  $$__/| $$                      | $$  /$$/          |__/          | $$        | $$               
   | $$   | $$$$$$$   /$$$$$$       | $$ /$$/  /$$$$$$$  /$$  /$$$$$$ | $$$$$$$  /$$$$$$             
   | $$   | $$__  $$ /$$__  $$      | $$$$$/  | $$__  $$| $$ /$$__  $$| $$__  $$|_  $$_/             
   | $$   | $$  \ $$| $$$$$$$$      | $$  $$  | $$  \ $$| $$| $$  \ $$| $$  \ $$  | $$               
   | $$   | $$  | $$| $$_____/      | $$\  $$ | $$  | $$| $$| $$  | $$| $$  | $$  | $$ /$$           
   | $$   | $$  | $$|  $$$$$$$      | $$ \  $$| $$  | $$| $$|  $$$$$$$| $$  | $$  |  $$$$/           
   |__/   |__/  |__/ \_______/      |__/  \__/|__/  |__/|__/ \____  $$|__/  |__/   \___/             
                                                             /$$  \ $$                               
                                                            |  $$$$$$/                               
                                                             \______/    Made by Naokimon""")
    sprint("1. New Game")
    sprint("2. Load Game")
    sprint("3. Exit Game")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_intro()
            break
        elif choice == 2:
            saved = load_game()
            if saved:
                print(f"Found saved game for {saved['name']}.")
                choice = inp("Load game? Y/N: ")
                if choice == "y":
                    player = Player.from_save(saved)
                elif choice == "n":
                    return True
            else:
                print("No saved game found.")
        elif choice == 3:
            break
main()