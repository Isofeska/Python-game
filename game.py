import Boss
import Enemy
import Player
import random
import os
import time

enemies = [Enemy.Enemy(5, 10, 2, 'goblin', 20, 2), Enemy.Enemy(7, 12, 5, 'skeleton', 20, 5), Enemy.Enemy(10, 13, 7, 'troll', 15, 10), Enemy.Enemy(10, 20, 5, 'minotaur', 10, 15), Enemy.Enemy(15, 15, 10, 'unknown soldier', 5, 20)]
bosses = [Boss.Boss(10, 20, 5, 'Goblin King', 20), Boss.Boss(14, 24, 7, 'Skeleton King', 25), Boss.Boss(10, 26, 10, 'Troll King', 30), Boss.Boss(15, 23, 10, 'Unknown King', 50)]

def attack(player, enemy, isPlayersTurn):
    if isPlayersTurn:
        if roll(1, 20, player.bonus) >= enemy.AC:
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
        if roll(1, 20, player.bonus) >= player.inventory[1].AC:
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

def boss_battle(player, level):
    boss = bosses[level]
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
                if Player.heal(player):
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
        if boss.name == 'Unknown King':
            player.complete_game = True
        if len(player.quest) == 1:
            if player.quest[0].task == 'Kill a boss':
                player.quest_progress += 1
        player.gold += boss.gold
        player.experience += 50
        player.turn = True
    else:
        player.isAlive = False

def battle(player):
    enemy = Enemy.pick_enemy(area_level, enemies)
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
                if Player.heal(player):
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
        if len(player.quest) == 1:
            if player.quest[0].task == 'Defeat enemies':
                player.quest_progress += 1
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
player = Player.Player(profession, name)

print(f'\nWelcome the forgotten land of brimstone! This land was once a place of prosperity and wealth, but is now rubble and ruin.')
print(f'This land has been overrun by monsters and otherwordly creatures alike. Your mission is to cleanse this place of the enemies that plague it.')
print(f'You should start laborous journey by killing the Goblin King. You will need to go into his territory and deal with his army along the way.')
print(f'Each boss you slay will bring you closer to your completing your task and will open each new area to kill the next boss.')
print(f'You can also head back to town to buy new gear, replenish flasks, and get new quests. Enough chat, you have monsters to slay!')

area_level = -1
level_intro = ['You head into a forest ruled by goblins...', 'You enter a dark cave creeping with skeletons and begin your next journey...', 'You enter the valley of trolls and begin your next journey...', 'You see a trail that climbs a mountains and begin your next journey...', 'You see a kingdom in ruins, you realize that you are near the end...']
started_journey = False

while (player.isAlive):
    if player.complete_game:
        os.system('cls')
        print(f'Congratulations you have finished the game!')
        break
    if player.in_town:
        print('\nWhat would you like to do?')
        ans = input('\n   1. Rest\n   2. Manage quests\n   3. Level up\n   4. Manage inventory\n   5. Show status\n   6. Shop\n   7. Leave\n')
        match ans:
            case '1':
                os.system('cls')
                if player.supplies > 10:
                    print('You decide to rest')
                    player.health += player.damage_taken
                    player.damage_taken = 0
                    player.supplies -= 10
                else:
                    print('Not enough camp supplies! You can get camp supplies by purchasing them at a shop')
            case '2':
                Player.manage_quest(player, Player.quests)
            case '3':
                os.system('cls')
                if player.experience <= player.experience_needed:
                    print('No level available!')
                else:
                    os.system('cls')
                    Player.lvlup(player)
                    print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
            case '4':
                Player.manage_inventory(player)
            case '5':
                os.system('cls')
                print(f'Vigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
                print(f'Health: {player.health} | Enemies slain: {player.enemies_killed} | Flasks: {player.flask_count}\nExperience: {player.experience} | Experience needed: {player.experience_needed}')
                print(f'Gold: {player.gold}')
            case '6':
                os.system('cls')
                Player.shop(player)
            case '7':
                os.system('cls')
                print('You leave town')
                player.in_town = False

    elif started_journey == False:
        print('\nWhat would you like to do?')
        ans = input('\n   1. Start journey!\n   2. Show status\n   3. Go to town\n   4. Manage inventory\n   5. Level up\n')
        match ans:
            case '1':
                os.system('cls')
                area_level += 1
                print(f'{level_intro[area_level]}')
                started_journey = True
                enemy_count = 5
                player.in_town = False

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
                os.system('cls')
                Player.manage_inventory(player)

            case '5':
                os.system('cls')
                if player.experience <= player.experience_needed:
                    print('No level available!')
                else:
                    Player.lvlup(player)
                    print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
    else:
        if enemy_count <= 0:
            print(f'You finally see the {bosses[area_level].name}!')
            boss_battle(player, area_level)
            area_level += 1
            started_journey = False
        else:
            print('\nWhat would you like to do?')
            ans = input('\n   1. Rest\n   2. Fight\n   3. Show status\n   4. Go to town\n   5. Manage inventory\n   6. Level up\n')
            match ans:
                case '1':
                    os.system('cls')
                    print('You decide to rest')
                    player.health += player.damage_taken
                    player.damage_taken = 0

                case '2':
                    if player.in_town == False:
                        os.system('cls')
                        battle(player)
                        enemy_count -= 1
                    else:
                        os.system('cls')
                        print('You cannot battle in town!')
                    if player.experience >= player.experience_needed:
                        print('Level up available!')
                    if len(player.quest) == 1:
                        if player.quest[0].task == 'Defeat enemies':
                            if player.quest_progress >= 5:
                                print('Quest complete!')
                        if player.quest[0].task == 'Kill a boss':
                            if player.quest_progress >= 1:
                                print('Quest complete!')

                case '3':
                    os.system('cls')
                    print(f'Vigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')
                    print(f'Health: {player.health} | Enemies slain: {player.enemies_killed} | Flasks: {player.flask_count}\nExperience: {player.experience} | Experience needed: {player.experience_needed}')
                    print(f'Gold: {player.gold}')

                case '4':
                    os.system('cls')
                    if player.in_town:
                        print('\nAlready in town!')
                    else:
                        print('You enter the village')
                        player.in_town = True

                case '5':
                    os.system('cls')
                    Player.manage_inventory(player)

                case '6':
                    os.system('cls')
                    if player.experience <= player.experience_needed:
                        print('No level available!')
                    else:
                        Player.lvlup(player)
                        print(f'\nVigor: {player.vigor} | Strength: {player.strength} | Dexterity: {player.dexterity}')

print('Game over')
