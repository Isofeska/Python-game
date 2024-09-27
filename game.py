import random
import os

class Player:
    #   inventory standard: 0: weapon, 1: armor, 2: talisman
    #   armor class, health, atk_damage, money
    #   vigor, strength, dexterity
    def __init__(self, CLASS, name):
        self.enemies_killed = 0
        self.turn = True
        self.experience = 0
        self.experience_needed = 20
        self.level = 0
        self.isAlive = True
        self.name = name
        self.money = 25
        self.damage_taken = 0
        self.level_available = False
        if CLASS == 'vagabond':#Vagabond class: Prioritizes defense above all
            self.weapon = 'halbred'
            self.armor = 'plate armor'
            self.AC = 16
            self.health = 15
            self.atk_damage = 4
            self.equipment = {self.weapon: self.atk_damage, self.armor: self.AC}
            self.inventory = {'flask': 10}
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        elif CLASS == 'warrior':#Warrior class: Yields higher damager for less defense
            self.weapon = 'battle axe'
            self.armor = 'chain mail'
            self.AC = 14
            self.health = 14
            self.atk_damage = 6
            self.equipment = {self.weapon: self.atk_damage, self.armor: self.AC}
            self.inventory = {'flask': 10}
            self.max_health = self.health
            self.vigor, self.strength, self.dexterity = 0, 0, 0
            self.crit_chance = 20

        else:#Rogue class: Prioritizes offense above all
            self.weapon = 'schimitar'
            self.armor = 'leather armor'
            self.AC = 12
            self.health = 12
            self.atk_damage = 10
            self.equipment = {self.weapon: self.atk_damage, self.armor: self.AC}
            self.inventory = {'flask': 10}
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

enemies = [Enemy(5, 10, 2, 'goblin', 20, 2), Enemy(7, 12, 5, 'skeleton', 20, 5), Enemy(10, 13, 7, 'troll', 15, 10), Enemy(10, 20, 5, 'minotaur', 10, 15), Enemy(15, 15, 10, 'unknown soldier', 5, 20)]
merchant_items = {''}
blacksmith_items = {''}

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
        player_attack = random.randint(1, player.crit_chance)
        if player_attack == player.crit_chance:
            print('Critical hit!')
            enemy.health -= player.atk_damage + 5
            enemy.damage_taken += player.atk_damage + 5
        else:
            enemy.health -= player.atk_damage
            enemy.damage_taken += player.atk_damage
    else:
        enemy_attack = random.randint(1, enemy.crit_chance)
        if enemy_attack == enemy.crit_chance:
            player.health -= enemy.atk_damage + 5
            player.damage_taken += enemy.atk_damage + 5
        else:
            player.health -= enemy.atk_damage
            player.damage_taken += enemy.atk_damage

def roll(min, max, bonus):
    min += bonus
    return random.randint(min, max)

def lvlup(player):
    choice = input('pick what to level: \n  1. vigor\n2. strength\n3. dexterity')
    if choice == '1':
        player.max_health += 10
        player.vigor += 1
    elif choice == '2':
        player.atk_damage += 5
        player.strength += 1
    else:
        player.atk_damage += 2
        player.crit_chance = player.crit_chance - 2
        player.dexterity += 1

def heal(player):
    for key, value in player.inventory:
        if key == 'flask':
            if player.health + value > player.max_health:
                player.health = player.max_health
                return True
            else:
                player.health += value
                return True
    print('No flask in inventory!')
    return False

def battle(player):
    enemy = pick_enemy(player.level, enemies)
    print(f'A {enemy.name} appears!')
    coward = False
    while(enemy.isAlive and player.isAlive):
        if player.turn:
            choice = input('What is your move?\n\n1. attack!\n2. heal\n3. run for your life\n')
            if choice == '1':
                os.system('clear')
                print(f'You attack the {enemy.name}!\n')
                attack(player, enemy, True)
                if enemy.health <= 0:
                    enemy.isAlive = False
                print(f'{enemy.name} health: {enemy.health}\n{player.name} health: {player.health}\n')
                player.turn = False
            elif choice == '2':
                os.system('clear')
                if heal(player):
                    player.turn = False
            else:
                os.system('clear')
                if random.randint(1,10) >= 5:
                    print(f'You live to see another day thanks to your legs')
                    coward = True
                    break
        else:
            os.system('clear')
            print(f'The {enemy.name} attacks you!\n')
            attack(player, enemy, False)
            if player.health <= 0:
                player.isAlive = False
            print(f'{player.name} health: {player.health}\n{enemy.name} health: {enemy.health}\n')
            player.turn = True

    if coward == False and player.isAlive:
        print('You slayed the monster!')
        player.experience += 20
        player.enemies_killed += 1
    enemy.health += enemy.damage_taken
    enemy.damage_taken = 0
    enemy.isAlive = True

name = input('What is your name, unfortunate soul? ')
profession = input('And what is your profession (pick vagabond, warrior, or rogue)? ')
player = Player(profession, name)

while (player.isAlive):
    print('\nWhat would you like to do?')
    ans = input('\n   1. Rest\n   2. Fight!\n   3. Show status\n   4. Shop\n   5. Manage inventory\n   6. Level up\n')
    if ans == '1':
        os.system('clear')
        print('You sleep as an escapism from your misery')
        player.health += player.damage_taken
        player.damage_taken = 0
    if ans == '2':
        os.system('clear')
        battle(player)
        if player.experience >= player.experience_needed:
            print('Level up available!')
            player.level_available = True
    if ans == '3':
        os.system('clear')
        print(f'Vigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
    if ans == '6':
        os.system('clear')
        if player.level_available == False:
            print('No level available!')
        else:
            lvlup(player)
            print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
print('You died...')
