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
        self.unit_class = {
            'swordmen': {'hp': 80, 'atk': 15},
            'archer': {'hp': 50, 'atk': 20 },
            'mage': {'hp': 40, 'atk': 25},
            'peasant levy': {'hp': 30, 'atk': 5}
        }
        if self.type not in self.unit_class:
            raise KeyError(f"{self.type} isn't avaliable to choose!")
        
        self.hp = self.unit_class[self.type]['hp']
        self.atk = self.unit_class[self.type]['atk']
        self.level = 1
        self.xp = 0
        self.xp_needed = 100
        self.XP_REQUIRED_INCREASE = 1.4
        self.matches = {
            'won': 0, 
            'lost': 0
        }
            
 
        
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.die()
            
    def attack(self, enemy):
        if self.alive and enemy.alive:
            damage = random.randint(int(self.atk * .5), int(self.atk * 1.3))
            enemy.take_damage(damage)
            print(f'\n{enemy.name} has suffered {damage} damage from {self.name}! \nHealth remaining: {enemy.hp}.')
            return damage
        else:
            return 0
        
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_needed:
            self.level += 1
            self.xp -= self.xp_needed
            self.xp_needed *= self.XP_REQUIRED_INCREASE
            self.hp += 5
            self.atk += 5
            print(f"Leveled up: {self.level}")
            
        
    def __str__(self):
        return f"\n{self.name} ({self.race} {self.type}) - Health: {self.hp}, Attack: {self.atk}, Experience: {self.xp}, Level: {self.level}\n"       
    
    def die(self):
        self.alive = False
   
    def match_stat(self, enemy):
    # Load existing cumulative stats (dict keyed by soldier name)
        try:
            with open('Battle_start.json', 'r') as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Ensure both entries exist
        if self.name not in data:
            data[self.name] = {"won": 0, "lost": 0}
        if enemy.name not in data:
            data[enemy.name] = {"won": 0, "lost": 0}

        # Add this match's results to the cumulative totals
        data[self.name]["won"] += self.matches.get("won", 0)
        data[self.name]["lost"] += self.matches.get("lost", 0)
        data[enemy.name]["won"] += enemy.matches.get("won", 0)
        data[enemy.name]["lost"] += enemy.matches.get("lost", 0)

        # Write back the updated cumulative stats
        with open('Battle_start.json', 'w') as f:
            json.dump(data, f, indent=2)

        # Print current cumulative standings
        print("==Cumulative Battle Status==")
        for name, match in data.items():
            print(f'{name}: {match}')
    
    def turn(self, enemy, delay=0.0):
        self._turn = False
        max_turn = 10
        all_turn = 0
        while self.alive and enemy.alive and all_turn < max_turn:
            time.sleep(delay)
            
            if all_turn % 2 == 0:
                enemy.attack(self)
                print(self)
            else:
                self.attack(enemy)
                print(enemy)
                
            all_turn +=1
        
        if not self.alive:
            print(f'Winner: {enemy.name}\n')
            enemy.matches["won"] += 1
            self.matches["lost"] += 1
            enemy.gain_xp(100)
        elif not enemy.alive:
            print(f'Winner: {self.name}\n')
            self.matches["won"] += 1
            enemy.matches["lost"] += 1
            self.gain_xp(100)
            
        elif all_turn == 10 and self.alive and enemy.alive:
            if self.hp > enemy.hp:
                print(f'Winner: {self.name}')
                self.matches["won"] += 1
                enemy.matches["lost"] += 1
                self.gain_xp(100)
            elif self.hp == enemy.hp:
                print('Tie')
            elif enemy.hp > self.hp:
                print(f'Winner: {enemy.name}')
                enemy.matches["won"] += 1
                self.matches["lost"] += 1
                enemy.gain_xp(100)
                    

        
def main():
    print("=== BATTLE ARENA ===")
    print("1. Quick Battle")
    print("2. Exit")
    choice = input("Choose: ")
    if choice == "1":
        # Your existing battle code
        human = Soldier("mage", "human", "Hero")
        human2 = Soldier('archer', 'elf', 'Enemy')
        human.turn(human2, 1)
        human.match_stat(human2)
        
if __name__ == "__main__":
    main()