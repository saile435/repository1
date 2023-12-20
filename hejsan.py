import random as rand




class character:
    def __init__(self, name, character_class, damage, hp, level, xp):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.damage = damage
        self.equipped_items = {"weapon": None, "healing": None}
        self.level = level
        self.xp = xp
        self.inventory = None

    def set_inventory(self, inventory):
        self.inventory = inventory

    def level_up(self):
        self.level += 1
        self.xp = 0
        print(f"You levelled up, your level is now: {self.level}")


    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            if weapon in self.inventory.items and self.inventory.items[weapon] > 0:
                previous_damage = self.damage
                self.equipped_items["weapon"] = weapon
                self.damage += weapon.damage
                added_damage = self.damage - previous_damage
                print(f"You have equipped {weapon.name}. Added {added_damage} damage.")
                self.inventory.remove_item(weapon)
            else:
                print("You don't have this weapon in your inventory.")
        else:
            print("You can only equip weapons.")

    def use_healing_item(self, healing_item):
        if isinstance(healing_item, heal):
            if healing_item in self.inventory.items and self.inventory.items[healing_item] > 0:
                previous_hp = self.hp
                self.equipped_items["healing"] = healing_item
                self.hp += healing_item.add_health
                healed_amount = self.hp - previous_hp
                print(f"You have used {healing_item.name} to heal. Healed {healed_amount} HP.")
                self.inventory.remove_item(healing_item)
            else:
                print("You don't have this healing item in your inventory.")
        else:
            print("You can only use healing items.")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.character_class}")
        print(f"Damage: {self.damage}")
        print(f"HP: {self.hp}")
        print(f"You level is: {self.level}")
        print("Equipped Items:")




def choose_character(player_inventory):
    character_1 = character("Ersnt-Rutger", 63, 85, 75, 1, 0)
    character_2 = character("Björn Örn", 47, 80, 90, 1, 0)
    character_3 = character("Britt-Inger", 89, 70, 100, 1, 0)
   
    print("Choose your character:")
    print("Option 1: Ernst-rutger, age = 63, power = 85, hp = 75")
    print("Option 2: Björn-örn, age = 47, power = 80, hp = 90")
    print("Option 3: Britt-Inger, age = 89, power = 70, hp = 100")
    choice = input("Choose your character please: ")
    while choice not in ['1', '2', '3']:
        print("Invalid answer")
        choice = input("Choose your character: ")
    if choice == '1':
        character_1.set_inventory(player_inventory)
        return character_1
    elif choice == '2':
        character_2.set_inventory(player_inventory)
        return character_2
    elif choice == '3':
        character_3.set_inventory(player_inventory)
        return character_3




class Weapon:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type


    def __str__(self):
        return self.name


Sword = Weapon("Sword", 5, "damaging")
Axe = Weapon("Axe", 10, "damaging")
Spear = Weapon("Spear", 8, "damaging")




class heal:
    def __init__(self, name, add_health, type):
        self.name = name
        self.add_health = add_health
        self.type = type
    def __str__(self):
        return self.name




mini_potion = heal("mini potion", 15, "healing")
big_potion = heal("big potion", 25, "healing")
kebabpizza = heal("kebabpizza", 35, "healing")




class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def use_items(self, item, hero):
        print("Enter how many of this item you want to use. Press Enter to cancel.")
        try:
            quantity = int(input())
        except ValueError:
            print("Invalid input. Cancelling.")
            return

        if quantity <= 0:
            print("Invalid quantity. Cancelling.")
            return

        if item in self.items and self.items[item] >= quantity:
            for _ in range(quantity):
                hero.use_healing_item(item) if isinstance(item, heal) else hero.equip_weapon(item)
            self.remove_item(item, quantity)
        else:
            print("Insufficient quantity in inventory.")


    def find_item(self, item_name):
        for item, quantity in self.items.items():
            if item.name.lower() == item_name.lower() and quantity > 0:
                return item
        return None




def trap(hero):
    print("You stepped in a trap and took damage!")
    trap_damage = rand.randint(10, 15)
    hero.hp -= trap_damage
    print(f"Your HP = {hero.hp}")
   
class mobs:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


    def __str__(self):
        return self.name


Goblin = mobs("Goblin", rand.randint(10,20), rand.randint(10, 15))
Zombie = mobs("Zombie", rand.randint(15, 25), rand.randint(10, 20))
Skeleton = mobs("Skeleton", rand.randint(25,30), rand.randint(15,25))
Ogre = mobs("Ogre", rand.randint(20,40), rand.randint(30,45))


def combat(hero, ):
    opponent = rand.choice([Goblin, Zombie, Skeleton, Ogre])
    print(f"You encounter a {opponent} with {opponent.damage} Strength and {opponent.hp} HP")
    if hero.hp//opponent.damage >= opponent.hp//hero.damage:
        hero.hp -= opponent.damage
        print(f"You won the fight, your hp is now {hero.hp}")
        hero.xp +=2
        print(f"You gained two xp, your xp is now: {hero.xp}")        
        if hero.xp >= 10:
            hero.level_up()
            hero.xp -= 10
        return hero
    elif opponent.hp//hero.damage < hero.hp//opponent.damage:
        print("You lost")
        hero.hp -= 1000
    else:
        pass
    return hero


def chest(player_inventory):
    item = rand.choice([Sword, Axe, Spear, mini_potion, big_potion, kebabpizza])
    print(f"You found {item.name}!")
    player_inventory.add_item(item)


def door_choices(hero, player_inventory):
    choice = rand.randint(0, 2)


    if choice == 0:
        trap(hero)
    elif choice == 1:
        chest(player_inventory)
    elif choice == 2:
        hero = combat(hero)


def main():
    player_inventory = Inventory()
    hero = choose_character(player_inventory)

    while hero.hp > 0 and hero.level < 10:
        print(
            """
            What do you want to do?
            1. Enter door
            2. Inventory
            3. Stats
            4. Use items
            """
        )
        val = input("")

        if val == "1":
            door_choices(hero, player_inventory)
        elif val == "2":
            player_inventory.display_inventory()
        elif val == "3":
            hero.display_details()
        elif val == "4":
            item_name = input("Enter the name of the item you want to use: ")
            item = player_inventory.find_item(item_name)
            if item:
                player_inventory.use_items(item, hero)
            else:
                print("Item not found in inventory.")
        else:
            print("Choose 1, 2, 3, or 4!")
    while hero.hp <= 0 or hero.level >= 10:
      break


main()