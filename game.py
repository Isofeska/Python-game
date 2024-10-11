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
            case 'nagakiba':
                self.price = 40
                self.atk_damage = 7
                self.description = 'A nagakiba from a far away land, no ones knows how it ended up here'
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

weapon = [Item('halbred'), Item('battle axe'), Item('schimitar'), Item('nagakiba'), Item('misericorde'), Item('greatsword')]
armor = [Item('armor plate'), Item('chail mail'), Item('leather armor'), Item('scale mail'), Item('padded armor'), Item('heavy armor plate')]
flask = Item('flask')

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
        self.flask_count = 1
        if CLASS == 'vagabond':
            self.health = 15
            self.inventory = [weapon[2], armor[2], flask]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        elif CLASS == 'warrior':
            self.health = 14
            self.inventory = [weapon[0], armor[0], flask]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        else:
            self.health = 12
            self.inventory = [weapon[1], armor[1], flask]
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

class Boss:

    def __init__(self, AC, health, atk_damage, name, gold):
        self.isAlive = True
        self.AC = AC
        self.health = health
        self.atk_damage = atk_damage
        self.name = name
        self.gold = gold

enemies = [Enemy(5, 10, 2, 'goblin', 20, 2), Enemy(7, 12, 5, 'skeleton', 20, 5), Enemy(10, 13, 7, 'troll', 15, 10), Enemy(10, 20, 5, 'minotaur', 10, 15), Enemy(15, 15, 10, 'unknown soldier', 5, 20)]
bosses = [Boss(10, 20, 5, 'Goblin King', 20), Boss(14, 24, 7, 'Skeleton King', 25), Boss(10, 26, 10, 'Troll King', 30), Boss(15, 23, 10, 'Unknown King', 50)]

def manage_inventory(player):
    done = False
    while done != True:
        answer5 = input(f'What do you want to do?\n   1. Equip items\n   2. See item descriptions\n')
        match answer5:
            case '1':
                if len(player.inventory) < 4:
                    print('No available items to equip!')
                else:
                    for i in range(3,len(player.inventory)):
                        if player.inventory[i] in weapon:
                            choice = input(f'Would you like to equip {player.inventory[i].name}? y or n: ')
                            if choice == 'y':
                                temp = player.inventory[0]
                                player.inventory[0] = player.inventory[i]
                                player.inventory[i] = temp
                                print('Successfully equipped!\n')
                                done = True

                        if player.inventory[i] in armor:
                            choice = input(f'Would you like to equip {player.inventory[i].name}? y or n: ')
                            if choice == 'y':
                                temp = player.inventory[1]
                                player.inventory[1] = player.inventory[i]
                                player.inventory[i] = temp
                                print('Successfully equipped!\n')
                                done = True
                    print('No other equippable items found')
                    done = True
            case '2':
                choice = input(f'What would you like to view?\n   1. {player.inventory[0].name}\n   2. {player.inventory[1].name}\n   3. {player.inventory[2].name}\n')
                match choice:
                    case '1':
                        print(player.inventory[0].description)
                        done = True
                    case '2':
                        print(player.inventory[1].description)
                        done = True
                    case '3':
                        print(player.inventory[2].description)
                        done = True


def pick_enemy(level, enemy_list):
    return enemy_list[level]


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
            print('Miss!\n')
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
            print('Miss!\n')

def roll(min, max, bonus):
    min += bonus
    return random.randint(min, max)

def shop(player):
    print(f'Current gold: {player.gold}')
    while True:
        pick = input('Welcome to the shop!\nPick out what you like:\n   1. flask(15)\n   2. nagakiba(40)\n   3. greatsword(50)\n   4. misericorde(45)\n   5. padded armor(30)\n   6. scale mail(40)\n   7. heavy armor plate(50)\n   8. Leave\n')
        match pick:
            case '1':
                if player.gold < 15:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.flask_count += 1
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
                        player.inventory[0] = weapon[3]
                    else:
                        player.inventory.append(weapon[3])
            case '3':
                if player.gold < 50:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 50
                    equip = input('Would you like to equip this item? y or n: ')
                    if equip == 'y':
                        player.inventory.append(player.inventory[0])
                        player.inventory[0] = weapon[5]
                    else:
                        player.inventory.append(weapon[5])
            case '4':
                if player.gold < 45:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 45
                    equip = input('Would you like to equip this item? y or n: ')
                    if equip == 'y':
                        player.inventory.append(player.inventory[0])
                        player.inventory[0] = weapon[4]
                    else:
                        player.inventory.append(weapon[4])
            case '5':
                if player.gold < 30:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 30
                    equip = input('Would you like to equip this item? y or n: ')
                    if equip == 'y':
                        player.inventory.append(player.inventory[1])
                        player.inventory[1] = armor[4]
                    else:
                        player.inventory.append(armor[4])
            case '6':
                if player.gold < 40:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 40
                    equip = input('Would you like to equip this item? y or n: ')
                    if equip == 'y':
                        player.inventory.append(player.inventory[1])
                        player.inventory[1] = armor[3]
                    else:
                        player.inventory.append(armor[3])
            case '7':
                if player.gold < 50:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 50
                    equip = input('Would you like to equip this item? y or n: ')
                    if equip == 'y':
                        player.inventory.append(player.inventory[1])
                        player.inventory[1] = armor[5]
                    else:
                        player.inventory.append(armor[5])
            case '8':
                break

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
                player.health = player.max_health
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
    if player.flask_count > 0:
        if player.health + 10 > player.max_health:
            player.health = player.max_health
        else:
            player.health += 10
        player.flask_count -= 1
    else:
        return False
    return True

def boss_battle(player):
    boss = bosses[area_level]
    print(f'The {boss.name} appears, ready yourself!')
    while (boss.isAlive and player.isAlive):
        if player.turn:
            choice = input('What is your move?\n\n   1. attack!\n   2. heal\n   3. defend\n')
            defend = False
            if choice == '1':
                os.system('cls')
                print(f'You attack the {boss.name}!\n')
                attack(player, boss, True)
                if boss.health <= 0:
                    boss.health = 0
                    boss.isAlive = False
                print(f'{boss.name} health: {boss.health}\n{player.name} health: {player.health}\n')
                player.turn = False
            elif choice == '2':
                os.system('cls')
                if heal(player):
                    print('You drink a flask')
                    print(f'{boss.name} health: {boss.health}\n{player.name} health: {player.health}\n')
                    player.turn = False
                else:
                    print('No flask in inventory!\n')
                    print(f'{boss.name} health: {boss.health}\n{player.name} health: {player.health}\n')
            else:
                defend = True
                os.system('cls')
                print('You choose to defend yourself')
                player.inventory[1].AC += 5
                player.turn = False
            time.sleep(2)
        else:
            os.system('cls')
            print(f'The {boss.name} attacks you!\n')
            attack(player, boss, False)
            if player.health <= 0:
                player.health = 0
                player.isAlive = False
            print(f'{boss.name} health: {boss.health}\n{player.name} health: {player.health}\n')
            player.turn = True
            if defend:
                player.inventory[1].AC -= 5
    if boss.isAlive == False:
        print(f'You slayed the {boss.name}!')
        player.gold += boss.gold
        player.experience += 20
        player.turn = True
        area_level += 1
        started_journey = False
        

def battle(player):
    enemy = pick_enemy(area_level, enemies)
    print(f'A {enemy.name} appears!')
    player_win = False
    while(enemy.isAlive and player.isAlive):
        if player.turn:
            choice = input('What is your move?\n\n1. attack!\n2. heal\n3. run for your life\n4. defend\n')
            defend = False
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
                    print('You drink a flask')
                    print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
                    player.turn = False
                else:
                    print('No flask in inventory!\n')
                    print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
            elif choice == '3':
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
                    print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
                    player.turn = True
            else:
                defend = True
                os.system('cls')
                print('You choose to defend yourself')
                player.inventory[1].AC += 5
                player.turn = False
            time.sleep(2)
        else:
            os.system('cls')
            print(f'The {enemy.name} attacks you!\n')
            attack(player, enemy, False)
            if player.health <= 0:
                player.health = 0
                player.isAlive = False
            print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
            player.turn = True
            if defend:
                player.inventory[1].AC -= 5

    if player_win:
        print('You slayed the monster!')
        player.gold += enemy.gold
        player.experience += 20
        player.enemies_killed += 1
        result = roll(0, 20, 0)
        if result >= enemy.flask_chance:
            player.flask_count += 1
    enemy.health = enemy.max_health
    enemy.isAlive = True
    player.turn = True

name = input('What is your name? ')
profession = input('And what is your profession (pick vagabond, warrior, or rogue)? ')
player = Player(profession, name)
print(f'Welcome the forgotten land of brimstone! This land was once a place of prosperity and wealth, but is now rubble and ruin.')
print(f'This land has been overrun by monsters and otherwordly creatures alike. Your mission is to cleanse this place of the enemies that plague it.')
print(f'You should start laborous journey by killing the Goblin King. You will need to go into his territory and deal with his army along the way.')
print(f'Each boss you slay will bring you closer to your completing your task and will open each new area to kill the next boss.')
print(f'You can also head back to town to buy new gear, replenish flasks, and get new quests. Enough chat, you have monsters to slay!')
area_level = -1
level_intro = ['You head into a forest ruled by goblins...']
started_journey = False

while (player.isAlive):
    if started_journey == False:
        print('\nWhat would you like to do?')
        ans = input('\n   1. Start journey!\n   2. Show status\n   3. Go to town\n   4. Manage inventory\n   5. Level up\n')
        match ans:
            case '1':
                os.system('cls')
                print(f'{level_intro[area_level]}')
                area_level += 1
                started_journey = True
                enemy_count = 5

            case '2':
                os.system('cls')
                print(f'Vigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
                print(f'Health: {player.health} | Enemies slain: {player.enemies_killed} | Flasks: {player.flask_count}\nExperience: {player.experience} | Experience needed: {player.experience_needed}')
                print(f'Gold: {player.gold}')

            case '3':
                os.system('cls')
                if player.in_town:
                    print('\nAlready in town!')
                else:
                    print('You enter the village')
                    player.in_town = True

            case '4':
                manage_inventory(player)

            case '5':
                os.system('cls')
                if player.experience <= player.experience_needed:
                    print('No level available!')
                else:
                    lvlup(player)
                    print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
    else:
        if enemy_count <= 0:
            print(f'You finally see the {enemies[area_level].name}!')
            battle()
        print('\nWhat would you like to do?')
        ans = input('\n   1. Rest\n   2. Fight\n   3. Show status\n   4. Go to town\n   5. Manage inventory\n   6. Level up\n')
        match ans:
            case '1':
                os.system('cls')
                print('You sleep as an escapism from your misery')
                player.health += player.damage_taken
                player.damage_taken = 0

            case '2':
                if player.in_town == False:
                    os.system('cls')
                    battle(player)
                    enemy_count -= 1
                if player.experience >= player.experience_needed:
                    print('Level up available!')
                else:
                    os.system('cls')
                    print('You cannot battle in town!')

            case '3':
                os.system('cls')
                if player.in_town:
                    print('\nAlready in town!')
                else:
                    print('You enter the village')
                    player.in_town = True

            case '4':
                manage_inventory(player)

            case '5':
                os.system('cls')
                if player.experience <= player.experience_needed:
                    print('No level available!')
                else:
                    lvlup(player)
                    print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')

print('Game over')
