import json
import time
import random
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
    def __init__(self, type_unit: str = "levy", race: str = "human", name: str = 'Regular Levy'):
        self.type = type_unit.lower()
        self.race = race.lower()
        self.name = name
        self.alive = True
        self.unit_clas = {
            'swordmen': {'hp': 80, 'atk': 15},
            'archer': {'hp': 50, 'atk': 20 },
            'mage': {'hp': 40, 'atk': 25},
            'peasant levy': {'hp': 30, 'atk': 5}
        }
        self.hp = self.unit_clas[self.type]['hp']
        self.atk = self.unit_clas[self.type]['atk']
        self._turn = False
        self.level = 0
        self.xp = 0
        self.xp_needed = 100
        self.matches = {
            'won': 0, 
            'lost': 0
        }
        
        if self.type not in self.unit_clas:
            raise KeyError(f"{self.type} isn't avaliable to choose!")
            
 
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.die()
            
    def attack(self, enemy):
        if self.alive and enemy.alive:
            damage = random.randint(int(self.atk * .5), int(self.atk * 1.3))
            enemy.take_damage(damage)
            enemy.attacker = self
            print(f'\n{enemy.name} has suffered {damage} damage from {self.name}! \nHealth remaining: {enemy.hp}.')
            return damage
        else:
            return 0
            
    def die(self):
        self.alive = False
        self.matches['lost'] += 1
        print(f'{self.name} has been defeated!')
        #enemy.xp_gain()
        
        if hasattr(self, "attacker"):
            self.attacker.matches['won'] += 1
            self.attacker.xp += 50
            # print(self.attacker.xp)
            
    def __str__(self):
        return f"\n{self.name} ({self.race} {self.type}) - Health: {self.hp}, Attack: {self.atk}\n"       
   
    def match_stat(self, enemy):
        status = {
            self.name: self.matches,
            enemy.name: enemy.matches
        }
    
        with open('Battle_start.json', 'w') as f:
            json.dump(status, f, indent=2)
            
        print("==Battle Status==")
        for name, match in status.items():
            print(f'{name}: {match}')
    
    def turn(self, enemy):
        self._turn = False
        max_turn = 10
        all_turn = 0
        while self.alive and enemy.alive and all_turn < max_turn:
            time.sleep(.8)
            
            if all_turn % 2 == 0:
                enemy.attack(self)
                print(self)
            else:
                self.attack(enemy)
                print(enemy)
                
            all_turn +=1

            if self.alive and enemy.alive:
                if self.hp > enemy.hp:
                        print(f'Winner: {self.name}')
                elif self.hp == enemy.hp:
                    print('Tie')
                elif enemy.hp > self.hp:
                    print(f'Winner: {enemy.name}')

        
        


human = Soldier("mage", "human", "hello")
human2 = Soldier('mage', 'human', 'guy')

human.turn(human2)

human.match_stat(human2)