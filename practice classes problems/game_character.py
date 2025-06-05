# Exercise: Create a GameCharacter class for a simple RPG game
# The character should:
# 1. Have name, health, level, and experience (xp)
# 2. Be able to gain xp and level up (every 100 xp = 1 level)
# 3. Take damage and heal
# 4. Show status (name, health, level, xp)
# 5. Have a special power that can only be used every 3 turns

class GameCharacter:
    def __init__(self, name, health=100):
        # Store name, health
        # Set initial level to 1, xp to 0
        # Add turns_until_special = 0 (for special power)
        self.name = name
        self.health = health
        self.level = 1
        self.xp = 0
        self.turns_until_special = 0
        
    
    def gain_xp(self, amount):
        # Add xp
        # Every 100 xp should increase level by 1
        # Print message when leveling up
        self.xp += amount
        while self.xp >= 100:
            self.level += 1
            self.xp -= 100
            print(f'Leveling up. Your new level is {self.level}')
        
    
    def take_damage(self, amount):
        # Reduce health by amount
        # Health can't go below 0
        # Return True if still alive, False if defeated
        if (self.health - amount) <= 0:
            return False
        else:
            self.health -= amount
            return True
        
    
    def heal(self, amount):
        # Add health (but not more than 100)
        if (self.health + amount) > 100:
            print("Cant go over maximum health(100).")
        else:
            self.health += amount
            return self.health
        
    
    def use_special_power(self):
        # Can only use if turns_until_special is 0
        # After using, set turns_until_special to 3
        # Return True if power was used, False if not ready
        if self.turns_until_special == 0:
            print('Using special ability!')
            self.turns_until_special = 3
        else:
            print("Ability not ready!!!")# Extended test:
        
    
    def end_turn(self):
        # Reduce turns_until_special by 1 (but not below 0)
        if self.turns_until_special >= 0:
            self.turns_until_special -= 1
        
    
    def show_status(self):
        # Show name, health, level, xp
        # Also show if special power is ready
        print(f"Name: {self.name}  Health: {self.health}  Level: {self.level}  Xp: {self.xp}")
        if self.turns_until_special == 0:
            print("Special Ability ready for use!!!")
        else:
            print(f'Ability will be available in {self.turns_until_special} turns!!!')

# Test your code:
# Extended test:
hero = GameCharacter("Hero")
hero.gain_xp(600)    # Should level up (100 XP = level 2)
hero.show_status()   # Should show level 2
hero.use_special_power()
hero.show_status()   # Special power should be on cooldown
hero.end_turn()      # Reduce cooldown by 1
hero.show_status()   # Should show cooldown reduced