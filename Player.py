import Item
import Quest
import random
import os

weapon = [Item.Item('halbred'), Item.Item('battle axe'), Item.Item('schimitar'), Item.Item('nagakiba'), Item.Item('misericorde'), Item.Item('greatsword')]
armor = [Item.Item('armor plate'), Item.Item('chain mail'), Item.Item('leather armor'), Item.Item('scale mail'), Item.Item('padded armor'), Item.Item('heavy armor plate')]
flask = Item.Item('flask')
quests = [Quest.Quest('Defeat enemies', 10, 5), Quest.Quest('Kill a boss', flask, 1), Quest.Quest('Defeat enemies', flask, 5), Quest.Quest('Kill a boss', 20, 1)]


class Player:

    def __init__(self, CLASS, name):
        self.supplies = 10
        self.complete_game = False
        self.quest = []
        self.quest_progress = 0
        self.gold = 0
        self.in_town = False
        self.bonus = 0
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
            self.inventory = [weapon[0], armor[0], flask]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        elif CLASS == 'warrior':
            self.health = 14
            self.inventory = [weapon[0], armor[1], flask]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        else:
            self.health = 12
            self.inventory = [weapon[2], armor[2], flask]
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 15

def get_quest(player, quests):
    os.system('cls')
    if len(player.quest) == 1:
        print('Quest already active!')
    else:
        player.quest.append(quests[random.randint(0,3)])

def complete_quest(player):
    os.system('cls')
    if len(player.quest) == 1:
        if player.quest_progress >= player.quest[0].required:
            print('Quest turned in!')
            if player.quest[0].reward == 10:
                player.gold += 10
            elif player.quest[0].reward == flask:
                player.flask_count += 1
            else:
                player.gold += 20
            del player.quest[0]
            player.quest_progress = 0
        else:
            print('Quest not completed!')
    else:
        print('No quest active!')

def manage_quest(player, quest):
    os.system('cls')
    while True:
        choice = input('What would you like to do?\n   1. Receive quest\n   2. Turn in quest\n   3. See active quest\n   4. Leave\n')
        match choice:
            case '1':
                if len(player.quest) == 1:
                    print('Quest already active!')
                else:
                    get_quest(player, quests)
                    print('Quest received!')
            case '2':
                complete_quest(player)
            case '3':
                if len(player.quest) == 0:
                    print('No active quests!')
                else:
                    os.system('cls')
                    print(f'task: {player.quest[0].task} | reward: gold or a flask | progress: {player.quest_progress}')
            case '4':
                os.system('cls')
                break

def shop(player):
    print(f'Current gold: {player.gold}\nWelcome to the shop!')
    while True:
        pick = input('Pick out what you like:\n   1. flask(15)\n   2. nagakiba(40)\n   3. greatsword(50)\n   4. misericorde(45)\n   5. padded armor(30)\n   6. scale mail(40)\n   7. heavy armor plate(50)\n   8. Camp Supplies\n   9. Leave\n')
        match pick:
            case '1':
                if player.gold < 15:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.flask_count += 1
                    player.gold -= 15
                    os.system('cls')
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
                    os.system('cls')
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
                    os.system('cls')
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
                    os.system('cls')
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
                    os.system('cls')
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
                    os.system('cls')
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
                        os.system('cls')
            case '8':
                if player.gold < 10:
                    print('Not enough money!')
                else:
                    print('Purchase successful!')
                    player.gold -= 10
                    player.supplies += 10
                    os.system('cls')

            case '9':
                os.system('cls')
                break

def manage_inventory(player):
    done = False
    while done != True:
        answer5 = input(f'What do you want to do?\n   1. Equip items\n   2. See item descriptions\n')
        match answer5:
            case '1':
                os.system('cls')
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
                os.system('cls')
                choice = input(f'What would you like to view?\n   1. {player.inventory[0].name}\n   2. {player.inventory[1].name}\n   3. {player.inventory[2].name}\n')
                match choice:
                    case '1':
                        os.system('cls')
                        print(player.inventory[0].description)
                        done = True
                    case '2':
                        os.system('cls')
                        print(player.inventory[1].description)
                        done = True
                    case '3':
                        os.system('cls')
                        print(player.inventory[2].description)
                        done = True


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
                player.bonus += 2
                picked = True
        else:
            if player.dexterity == player.max_dexterity:
                print('Already max level!')
            else:
                player.inventory[0].atk_damage += 2
                player.crit_chance = player.crit_chance - 2
                player.dexterity += 1
                player.bonus += 2
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
