import json


def character_to_dict(character):
    dict_character = {
        "name": character.name,
        "class": character.character_class,

        "health": character.health,
        "mana": character.mana,

        "strength": character.strength,
        "defense": character.defense,
        "level": character.level,
        "experience": character.experience,
        "max_experience": character.max_experience,
        "gold": character.gold,
        "max_health": character.max_health,
        "max_mana": character.max_mana,

        "statistics" : statistics_to_dict(character.statistics),
        "inventory": inventory_to_list(character.inventory)
    }

    return dict_character

def statistics_to_dict(statistics):
    dict_statistics = {
        "enemies_killed" : statistics.enemies_killed,
        "bosses_killed" : statistics.bosses_killed,
        "rooms_completed" : statistics.rooms_completed,
        "gold_earned" : statistics.gold_earned,
        "damage_taken" : statistics.damage_taken
    }
    return dict_statistics

def item_to_dict(item):
    dict_item = {
        "name": item.name,
        "item_type": item.item_type,
        "value" : item.value,
        "effect_value" : item.effect_value,
    }
    return dict_item

def inventory_to_list(inventory):
    list_inventory = []
    for item in inventory.items:
        list_inventory.append(item_to_dict(item))

    return list_inventory






def save_character(character):
    character_data = character_to_dict(character)
    with open("save.json", "w") as file:
        json.dump(character_data, file, indent=4, ensure_ascii=False)


