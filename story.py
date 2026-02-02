from player import Player
from utils import inp, sprint, cls, dprint

invalid = "Enter a valid answer"

def show_intro():
    cls()
    while True:
        name = input("Enter your name: ")
        player = Player(name)
        print(f"Your name is {name}. Is that correct? Y/N")
        answer = inp()
        if answer == "y":
            break
        elif answer == "n":
            print("Try again.")
        else:
            print(invalid)

    cls()
    sprint(r"""
 /$$      /$$           /$$                                                     /$$                  
| $$  /$ | $$          | $$                                                    | $$                  
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$  /$$
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$|__/
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$    
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$ /$$
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/|__/
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/     
                                                                                                     
                                                                                                     
                                                                                                     
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
                                                             \______/                Made by Naokimon
    """)
    input("Press enter to continue.")

    cls()
    print(f"You are {name}, a knight. You were on an quest with your banner.A quest off to a place far away from your kingdom near exotic lands. That is were you met...")
    while True:
        petname = input("Enter the name of your pet monkey: ")
        player.pet_name = petname
        print(f"Your pet monkey's name is {petname}. Is that correct? Y/N")
        answer = inp()
        if answer == "y":
            break
        elif answer == "n":
            print("Try again.")
        else:
            print(invalid)
    cls()
    dprint(f"You are {name}, a knight. You were on a quest with your banner.A quest off to a place far away from your kingdom near")
    dprint(f"exotic lands. That is were you met {petname}. You and {petname} were best of friends, inseparable even. Then it")
    dprint(f"was time to leave. The leader of your banner... a ruthless knight named Tidor. He opposed your request to keep")
    dprint(f"{petname}. Without thinking you took them with you anyway. You snuck them with you. While traveling back to your")
    dprint(f"kingdom Zekerilya, Tidor noticed your monkey with you. Disobeying a direct order can be punishable to death...")
    dprint(f"Fear stricken you ran away as far as you could. Your fellow knights caught you. Tidor took {petname} from your grasp.")
    dprint(f"He stole {petname} and took them into a cage. On the way back to the kingdom you were shackled. Your banner stopped")
    dprint("a few miles before entering in the kingdom. On Tidor's command your fellow friends dropped you for dead in a swamp,")
    dprint(f"riddled with slimes and other such unnatural's... As you take a look at {petname}'s eyes for the last time you see Tidor's")
    dprint("fist heading towards your face...")
    print("")
    dprint(f"Your story begins here {name}...")
    input("Press enter to continue")