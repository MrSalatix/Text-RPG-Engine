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

    def take_damage(self, amount_damage):
        if amount_damage >= 0:
            self.health -= amount_damage
            if self.health <= 0:
                self.health = 0
        return self.health

    def heal(self, amount_heal):
        if amount_heal >= 0:
            self.health += amount_heal
            if self.health >= self.max_health:
                self.health = self.max_health
        return self.health

    def spend_mana(self, amount_mana):
        if amount_mana >= 0:
            if self.mana >= amount_mana:
                self.mana -= amount_mana
                return True
            else:
                return False
        else:
            return False

    def restore_mana(self, amount_mana):
        if amount_mana >= 0:
            self.mana += amount_mana
            if self.mana >= self.max_mana:
                self.mana = self.max_mana
        return self.mana

    def add_gold(self, amount_gold):
        if amount_gold >= 0:
            self.gold += amount_gold
        return self.gold

    def spend_gold(self, amount_gold):
        if amount_gold >= 0:
            if self.gold >= amount_gold:
                self.gold -= amount_gold
                return True
            else:
                return False
        else:
            return False

    def is_alive(self):
        return self.health > 0




