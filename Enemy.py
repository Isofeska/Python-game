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
        
def pick_enemy(level, enemy_list):
    return enemy_list[level]
