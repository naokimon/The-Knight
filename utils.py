import time, sys, os, json

SAVE_FILE = ("save.json")

def save_game(player):
    data = {
        "name": player.name,
        "pet_name": player.pet_name,
        "hp": player.hp,
        "inventory": player.inventory
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("Game saved!")

def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sprint(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def dprint(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def inp(prompt=""):
    return input(prompt).strip().lower()



