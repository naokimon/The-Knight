class Player:
    def __init__(self, name):
        self.name = name
        self.pet_name = None
        self.health = 100
        self.mana = 25
        self.attack = 5
        self.inventory = []

    @classmethod
    def from_save(cls, data):
        player = cls(data["name"])
        player.pet_name = data.get("pet_name")
        player.hp = data.get("hp", 20)
        player.inventory = data.get("inventory", [])
        return player
