class Character:

    def __init__(self, name, character_class, health, mana, strength, defense, max_health, max_mana):
        self.name = name
        self.character_class = character_class

        self.health = health
        self.mana = mana

        self.strength = strength
        self.defense = defense
        self.level = 1
        self.experience = 0
        self.gold = 0
        self.max_health = max_health
        self.max_mana = max_mana
    def describe_character(self):  #решил сделать так как удобнее
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


