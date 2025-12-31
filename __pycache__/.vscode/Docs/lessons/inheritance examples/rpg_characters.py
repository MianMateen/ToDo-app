class GameCharacter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.max_health = health
        self.level = 1
        self.xp = 0
        self.turns_until_special = 0
        self.damage = 10

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= 100:
            self.level += 1
            self.xp -= 100
            print(f'Leveling up. Your new level is {self.level}')
    
    def attack(self, target):
        target.take_damage(self.damage)
        print(f"{self.name} attacks {target.name} for {self.damage} Damage!")

    def alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        return self.health > 0
        
    def heal(self, amount):
        if (self.health + amount) > self.max_health:
            print("Can't go over maximum health.")
        else:
            self.health += amount
            return self.health
        
    def use_special_power(self, target):
        if self.turns_until_special == 0:
            self.damage = 20
            target.take_damage(self.damage)
            self.turns_until_special = 3
            print(f'{self.name} uses special ability on {target.name}!')
            return True
        else:
            print("Ability not ready!")
            return False
        
    def end_turn(self):
        if self.turns_until_special >= 0:
            self.turns_until_special -= 1
        
    def show_status(self):
        print(f"\nName: {self.name}  Health: {self.health}  Level: {self.level}  Xp: {self.xp}")
        if self.turns_until_special == 0:
            print("Special Ability ready for use!!!")
        else:
            print(f'Ability will be available in {self.turns_until_special} turns!!!\n')


class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=150)
        self.strength = 15
        self.armor = 5
    
    def attack(self, target):
        target.take_damage(self.strength)
        print(f"{self.name} attacks {target.name} for {self.strength} Damage!")

    def take_damage_warrior(self, amount):  
        damage = max(0, amount - self.armor)
        self.health = max(0, self.health - damage)
        return self.health > 0

    def use_special_power(self, target):
        if self.turns_until_special == 0:
            print(f"{self.name} uses Mighty Strike!")
            self.turns_until_special = 3
            self.damage = self.strength * 2
            target.take_damage(self.damage)
            print(f'{self.name} uses special ability on {target.name}!')
            return True
        else:
            print("Ability not ready!")
            return False


class Mage(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=80)
        self.magic = 15
        self.mana = 100
    
    def attack(self, target):
        if isinstance(target, Warrior):
            target.take_damage_warrior(self.magic)
        else:
            target.take_damage(self.magic)
        print(f"{self.name} attacks {target.name} for {self.magic} Damage!")

    def use_special_power(self, target):
        if self.turns_until_special == 0 and self.mana >= 50:
            print(f"{self.name} casts Fireball!")
            self.mana -= 50
            self.turns_until_special = 2
            self.damage = self.magic * 3
            target.take_damage(self.damage)
            print(f'{self.name} uses special ability on {target.name}!')
            return True
        else:
            print("Not enough mana or ability not ready!")
            return False


def battle(char1, char2):
    print(f"\n-- {char1.name} vs {char2.name} --\n")
    turns = 10
    while turns != 0:
        # Character 1's turn
        print(f"\n{char1.name}'s turn:")
        if char1.turns_until_special == 0:
            char1.use_special_power(char2)
        else:
            char1.attack(char2)
        char1.end_turn()
        
        # Check if character 2 is defeated
        if not char2.alive():
            print(f"{char2.name} has been defeated!")
            print(f"\n{char1.name} wins the battle!")
            break
        
        # Character 2's turn
        print(f"\n{char2.name}'s turn:")
        if char2.turns_until_special == 0:
            char2.use_special_power(char1)
        else:
            char2.attack(char1)
        char2.end_turn()
        
        # Check if character 1 is defeated
        if not char1.alive():
            print(f"{char1.name} has been defeated!")
            print(f"\n{char2.name} wins the battle!")
            break
        
        turns -= 1
        # Show status after each round
        char1.show_status()
        char2.show_status()



def battle_test():
    char1 = Warrior("Conan")
    char2 = Mage("Gandalf")
    battle(char1, char2)


if __name__ == "__main__":
    battle_test()