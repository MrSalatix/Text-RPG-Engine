def damage_calculator(amount_strength, amount_defense):
    amount_damage = amount_strength
    if amount_damage > amount_defense:
        amount_damage -= amount_defense
        return amount_damage
    else:
        amount_damage = 1
    return amount_damage

def combat(character, enemy):
    character_damage = damage_calculator(character.strength, enemy.defense)
    enemy_damage = damage_calculator(enemy.strength, character.defense)

    print("================COMBAT================")
    print(f"{character.name} VS {enemy.name}")
    print("======================================")
    while character.is_alive() and enemy.is_alive():
        enemy.take_damage(character_damage)
        print(f"{character.name} атакует {enemy.name}, нанося {character_damage} урона!")
        print(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
        if enemy.is_alive():
            character.take_damage(enemy_damage)
            print(f"{enemy.name} атакует {character.name}, нанося {enemy_damage} урона!")
            print(f"{character.name} HP: {character.health}/{character.max_health}")
            if character.is_alive():
                continue
            else:
                print(f"{character.name} погиб! Вы проиграли:(")
                break
        else:
            print(f"{enemy.name} повержен!")
            break



