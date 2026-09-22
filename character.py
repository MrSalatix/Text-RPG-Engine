class Character:
    maxhealth = 100
    max_mana = 100
    gold = 0
    level = 1
    experience = 0
    def __init__(self, name, character_class, health, mana, strength, defense):
        self.name = name
        self.character_class = character_class

        self.health = health
        self.mana = mana

        self.strength = strength
        self.defense = defense
