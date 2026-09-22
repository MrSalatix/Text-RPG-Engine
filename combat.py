def damage_calculator(amount_damage, amount_defense):
    if amount_damage > amount_defense:
        amount_damage -= amount_defense
        return amount_damage
    else:
        amount_damage = 1
    return amount_damage

def combat(character, enemy):
    while character.is_alive() and enemy.is_alive():
        enemy.take_damage(damage_calculator(character.strength, enemy.defense))
        if enemy.is_alive():
            character.take_damage(damage_calculator(enemy.strength, character.defense))
            if character.is_alive():
                continue
            else:
                break
        else:
            break



