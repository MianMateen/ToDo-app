# class Unit: # Note that the smallest combat functioning unit is a company (100 troops): (Swordsmen/Spearmen: 60), (Archers: 30), (Elites: 10).
#     def __init__(self, type_unit, mele, ranged, elites, kingdom):
#         self.type = type_unit.lower()
#         self.mele = mele
#         self.ranged = ranged
#         self.elites = elites
#         self.kingdom = kingdom.capitalize()
        
#         if self.type == 'company':
#             self.size = 100
#             self.army_in_terms_of_companies = [50]
#             print(f"Kingdom of {self.kingdom}'s {self.army_in_terms_of_companies[45]} Company.")
    
#     def action(self, action, which_unit_flank=None):
#         self.which_unit_flank = which_unit_flank
#         self.action = action
#         self.commands = set('advance', 'halt', 'retreat', 'fallback')
#         if self.action not in self.commands:
#             print('Not valid movement')
#         print(f'{self.which_unit_flank} {self.direction} towards enemy.')
        
#     def attack(self):
#         self.units_attack_power = (self.mele * 3) + (self.ranged * 3) + (self.elites * 6)

class Soldier:
    def __init__(self, type_unit: str = "Levy", race: str = "Human", name: str = 'Regular Levy'):
        self.type = type_unit
        self.race = race
        self.name = name
        self.alive = True
        self.unit_clas = {
            'swordmen': {'hp': 80, 'atk': 15},
            'archer': {'hp': 50, 'atk': 20 },
            'mage': {'hp': 40, 'atk': 25},
            'Peasant Levy': {'hp': 30, 'atk': 5}
        }
        self.hp = self.unit_clas[self.type]['hp']
        self.atk = self.unit_clas[self.type]['atk']
        
        if self.type in self.unit_clas:
            print(f"{self.type} isn't avaliable to choose!")
        else:
            pass
        
    def __str__(self):
        return f"\n{self.name} ({self.race} {self.type}) - Health: {self.unit_clas[self.type]['hp']}, Attack: {self.unit_clas[self.type]['atk']}\n"
    
    def attack(self, enemy):
        if self.alive and enemy.alive:
            damage = self.unit_clas[self.type]['atk']
            enemy.take_damage(damage)
            if enemy.hp <= 0:
                enemy.hp = 0
            print(f'\n{enemy.name} has suffered {damage} damage from {self.name}! \nHealth remaining: {self.hp}.')
            return damage
        else:
            return 0
            
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()
            
    def die(self):
        self.alive = False
        print(f'{self.name} has been defeated!')
    
Human = Soldier('swordmen', 'Human', 'Baldin')
Human2 = Soldier('mage', 'human', 'Storkil')


while Human.alive and Human2.alive:
    Human2_turn = True
    
    
    if Human2_turn:
        Human2.attack(Human)
        Human2_turn = False
    else:
        Human.attack(Human2)
        Human2_turn = True