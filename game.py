import random
import os
import time

class Item:
    def __init__(self, name):
        self.name = name
        match name:
            case 'padded armor':
                self.price = 30
                self.AC = 14
                self.description = 'A padded armor piece that provides protection and freedom of movement'
            case 'scale mail':
                self.price = 40
                self.AC = 16
                self.description = 'A sturdy piece of scale mail that will endure the bluntest attack and harshest weather'
            case 'heavy armor plate':
                self.price = 50
                self.AC = 18
                self.description = 'A heavy piece of armor that provides maximum protection'
            case 'greatsword':
                self.price = 50
                self.atk_damage = 8
                self.description = 'A large sword more fitting to called a slab of iron'
            case 'misericorde':
                self.price = 45
                self.atk_damage = 4
                self.description = 'A sharp dagger that packs a powerful punch when you land a critical hit'
            case 'nagikiba':
                self.price = 40
                self.atk_damage = 7
                self.description = 'A nagikiba from a far away land, no ones knows how it ended up here'
            case 'halbred':
                self.atk_damage = 5
                self.description = 'A battle-hardened halbred that will strike enemies from a distance'
            case 'battle axe':
                self.atk_damage = 5
                self.description = 'A battle-worn axe that strikes true'
            case 'schimitar':
                self.atk_damage = 5
                self.description = 'A shiny schimitar eager for battle'
            case 'armor plate':
                self.AC = 16
                self.description = 'A reliable piece of metal armor that will protect you from enemy attacks'
            case 'chain mail':
                self.AC = 14
                self.description = 'A piece of chain mail that will provide extra protection'
            case 'leather armor':
                self.AC = 12
                self.description = 'A piece of leather armor that provides poor protection for enhanced mobility'
            case 'flask':
                self.price = 15
                self.flask_count = 1
                self.description = 'A potion of healing that you can use while in combat'

class Player:

    #   inventory standard: 0: weapon, 1: armor, 2: Flask

    def __init__(self, CLASS, name):
        self.gold = 0
        self.in_town = False
        self.max_vigor = 4
        self.max_strength = 4
        self.max_dexterity = 4
        self.enemies_killed = 0
        self.turn = True
        self.experience = 0
        self.experience_needed = 30
        self.level = 0
        self.isAlive = True
        self.name = name
        self.damage_taken = 0
        if CLASS == 'vagabond':
            self.health = 15
            self.inventory = [Item('halbred'), Item('armor plate'), Item('flask')]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        elif CLASS == 'warrior':
            self.health = 14
            self.inventory = [Item('battle axe'), Item('chain male'), Item('flask')]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        else:
            self.health = 12
            self.inventory = [Item('schimitar'), Item('leather armor'), Item('flask')]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 15

class Enemy:

    def __init__(self, AC, health, atk_damage, name, flask_chance, gold):
        self.damage_taken = 0
        self.isAlive = True
        self.AC = AC
        self.health = health
        self.atk_damage = atk_damage
        self.name = name
        self.crit_chance = 20
        self.flask_chance = flask_chance
        self.gold = gold
        self.max_health = health

enemies = [Enemy(5, 10, 2, 'goblin', 20, 2), Enemy(7, 12, 5, 'skeleton', 20, 5), Enemy(10, 13, 7, 'troll', 15, 10), Enemy(10, 20, 5, 'minotaur', 10, 15), Enemy(15, 15, 10, 'unknown soldier', 5, 20)]

def pick_enemy(level, enemy_list):
    if level == 0:
        return enemy_list[random.randint(0,1)]
    elif level == 1:
        return enemy_list[random.randint(1,2)]
    elif level == 2:
        return enemy_list[random.randint(2,3)]
    else:
        return enemy_list[random.randint(3,4)]

def attack(player, enemy, isPlayersTurn):
    if isPlayersTurn:
        if roll(1, 20, 0) >= enemy.AC:
            player_attack = random.randint(1, player.crit_chance)
            if player_attack == player.crit_chance:
                print('Critical hit!')
                if player.inventory[0].name == 'Misericorde':
                    enemy.health -= player.inventory[0].atk_damage + 10
                else:
                    enemy.health -= player.inventory[0].atk_damage + 5
            else:
                enemy.health -= player.inventory[0].atk_damage
        else:
            print('Miss!')
    else:
        if roll(1, 20, 0) >= player.inventory[1].AC:
            enemy_attack = random.randint(1, enemy.crit_chance)
            if enemy_attack == enemy.crit_chance:
                print('Critical hit!')
                player.health -= enemy.atk_damage + 5
                player.damage_taken += enemy.atk_damage + 5
            else:
                player.health -= enemy.atk_damage
                player.damage_taken += enemy.atk_damage
        else:
            print('Miss!')

def roll(min, max, bonus):
    min += bonus
    return random.randint(min, max)

def shop(player):
    pick = input('Welcome to the shop!\nTake a look at the wares:\n   1. flask\n   2. nagikiba\n   3. greatsword\n   4. misericorde\n   5. padded armor\n   6. scale mail\n   7. heavy armor plate\n')
    match pick:
        case '1':
            if player.gold < 15:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.inventory[2].flask_count += 1
                player.gold -= 15
        case '2':
            if player.gold < 40:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 40
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[0])
                    player.inventory[0] = Item('nagikiba')
                else:
                    player.inventory.append(Item('nagikiba'))
        case '3':
            if player.gold < 50:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 50
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[0])
                    player.inventory[0] = Item('greatsword')
                else:
                    player.inventory.append(Item('greatsword'))
        case '4':
            if player.gold < 45:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 45
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[0])
                    player.inventory[0] = Item('misericorde')
                else:
                    player.inventory.append(Item('misericorde'))
        case '5':
            if player.gold < 30:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 30
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[1])
                    player.inventory[1] = Item('padded armor')
                else:
                    player.inventory.append(Item('padded armor'))
        case '6':
            if player.gold < 40:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 40
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[1])
                    player.inventory[1] = Item('scale mail')
                else:
                    player.inventory.append(Item('scale mail'))
        case '7':
            if player.gold < 50:
                print('Not enough money!')
            else:
                print('Purchase successful!')
                player.gold -= 50
                equip = input('Would you like to equip this item? y or n: ')
                if equip == 'y':
                    player.inventory.append(player.inventory[1])
                    player.inventory[1] = Item('heavy armor plate')
                else:
                    player.inventory.append(Item('heavy armor plate'))
def lvlup(player):
    picked = False
    while picked == False:
        choice = input('pick what to level: \n  1. vigor\n  2. strength\n  3. dexterity\n**To cancel enter stop**\n')
        if choice == 'stop':
            break
        if choice == '1':
            if player.vigor == player.max_vigor:
                print('Already max level!')
            else:
                player.max_health += 10
                player.vigor += 1
                picked = True
        elif choice == '2':
            if player.strength == player.max_strength:
                print('Already max level!')
            else:
                player.inventory[0].atk_damage += 5
                player.strength += 1
                picked = True
        else:
            if player.dexterity == player.max_dexterity:
                print('Already max level!')
            else:
                player.inventory[0].atk_damage += 2
                player.crit_chance = player.crit_chance - 2
                player.dexterity += 1
                picked = True
        
        if picked == True:
            player.experience -= player.experience_needed
            player.experience_needed = player.experience_needed * 2
            player.level += 1

def heal(player):
    if player.inventory[2].flask_count < 0:
        print('No flask in inventory!')
        return False
    else:
        if player.health + player.inventory[2].flask_count > player.max_health:
            player.health = player.max_health
        else:
            player.health += 10
        player.inventory[2].flask_count -= 1


def battle(player):
    enemy = pick_enemy(player.level, enemies)
    print(f'A {enemy.name} appears!')
    player_win = False
    while(enemy.isAlive and player.isAlive):
        if player.turn:
            choice = input('What is your move?\n\n1. attack!\n2. heal\n3. run for your life\n')
            if choice == '1':
                os.system('cls')
                print(f'You attack the {enemy.name}!\n')
                attack(player, enemy, True)
                if enemy.health <= 0:
                    enemy.health = 0
                    player_win = True
                    enemy.isAlive = False
                print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
                player.turn = False
            elif choice == '2':
                os.system('cls')
                if heal(player):
                    player.turn = False
            else:
                os.system('cls')
                if random.randint(1,10) >= 5:
                    print(f'You live to see another day thanks to your legs')
                    break
                else:
                    print(f'The {enemy.name} attacks you!\n')
                    attack(player, enemy, False)
                    if player.health <= 0:
                        player.health = 0
                        player.isAlive = False
                    print(f'{player.name} health: {player.health}\n{enemy.name} health: {enemy.health}\n')
                    player.turn = True
            time.sleep(2)
        else:
            os.system('cls')
            print(f'The {enemy.name} attacks you!\n')
            attack(player, enemy, False)
            if player.health <= 0:
                player.health = 0
                player.isAlive = False
            print(f'{player.name} health: {player.health}\n{enemy.name} health: {enemy.health}\n')
            player.turn = True

    if player_win:
        print('You slayed the monster!')
        player.gold += enemy.gold
        player.experience += 20
        player.enemies_killed += 1
    enemy.health = enemy.max_health
    enemy.isAlive = True
    player.turn = True

name = input('What is your name, unfortunate soul? ')
profession = input('And what is your profession (pick vagabond, warrior, or rogue)? ')
player = Player(profession, name)

while (player.isAlive):
    print('\nWhat would you like to do?')
    ans = input('\n   1. Rest\n   2. Fight!\n   3. Show status\n   4. Go to town\n   5. Manage inventory\n   6. Level up\n   7. Shop\n   8. Leave\n')
    if ans == '1':
        os.system('cls')
        print('You sleep as an escapism from your misery')
        player.health += player.damage_taken
        player.damage_taken = 0
    if ans == '2':
        if player.in_town == False:
            os.system('cls')
            battle(player)
            if player.experience >= player.experience_needed:
                print('Level up available!')
        else:
            print('You cannot battle in town!')
    if ans == '3':
        os.system('cls')
        print(f'Vigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
        print(f'Health: {player.health} | Enemies slain: {player.enemies_killed} | Flasks: {player.inventory[2].flask_count}\nExperience: {player.experience} | Experience needed: {player.experience_needed}')
        print(f'Gold: {player.gold}')
    if ans == '4':
        player.in_town = True
    if ans == '5':
        temp = input(f'What would you look to view?\n1. {player.inventory[0].name}\n2. {player.inventory[1].name}\n')
        if temp == '1':
            print(f'{player.inventory[0].description}')
        else:
            print(f'{player.inventory[1].description}')
    if ans == '6':
        os.system('cls')
        if player.experience <= player.experience_needed:
            print('No level available!')
        else:
            lvlup(player)
            print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
    if ans == '7':
        if player.in_town:
            shop(player)
        else:
            print('You must be town to shop!')
    if ans == 8:
        if player.in_town:
            print('You leave town')
        else:
            choice = input('Are you sure? y or n: ')
            if choice == 'y':
                break
print('You died...')
