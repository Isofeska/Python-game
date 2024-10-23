class Boss:

    def __init__(self, AC, health, atk_damage, name, gold):
        self.isAlive = True
        self.AC = AC
        self.health = health
        self.atk_damage = atk_damage
        self.name = name
        self.gold = gold
        self.crit_chance = 20
