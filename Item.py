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

