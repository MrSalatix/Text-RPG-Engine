class Character:
    def __init__(self, name, character_class, health, mana, strength, defense, experience, gold, level, max_health, max_mana):
        self.name = name
        self.character_class = character_class

        self.health = health
        self.mana = mana

        self.strength = strength
        self.defense = defense

        self.max_health = max_health
        self.max_mana = max_mana
        self.gold = gold
        self.level = level
        self.experience = experience
    def __str__(self):
        print('== == == == == == == == == ==')
        print('CHARACTER')

        print(f'Name: ', self.name)
        print(f'Class: ', self.character_class)
        print(f'Level: ', self.level)
        print(f'Exp: ', self.experience)

        print(f'HP: {self.health} / {self.max_health}')
        print(f'Mana: {self.mana} / {self.max_mana}')

        print(f'Strength: ', self.strength)
        print(f'Defense: ', self.defense)

        print(f'Gold: ', self.gold)
        print('== == == == == == == == == ==')


