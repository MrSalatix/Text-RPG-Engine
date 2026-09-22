class Character:

    def __init__(self, name, character_class, strength, defense, max_health, max_mana):
        self.name = name
        self.character_class = character_class

        self.health = max_health
        self.mana = max_mana

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

        print('Name: ', self.name)
        print('Class: ', self.character_class)
        print('Level: ', self.level)
        print('Exp: ', self.experience)

        print(f'HP: {self.health} / {self.max_health}')
        print(f'Mana: {self.mana} / {self.max_mana}')

        print('Strength: ', self.strength)
        print('Defense: ', self.defense)

        print('Gold: ', self.gold)
        print('== == == == == == == == == ==')


