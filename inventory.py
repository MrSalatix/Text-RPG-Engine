class Inventory:
    def __init__(self, max_capacity):
        self.items = []
        self.max_capacity = max_capacity

    def add_item(self, item):
        if len(self.items) < self.max_capacity:
            self.items.append(item)
            print("Предмет добавлен")
        else:
            print("Инвентарь переполнен!")

    def show_inventory(self):
        if len(self.items) != 0:
            print("Инвентарь: ")
            for i in self.items:
                i.describe_item()
        else:
            print("Инвентарь пуст!")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Предмет удален")
        else:
            print("Нет такого предмета!")



