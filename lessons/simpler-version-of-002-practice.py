# Exercise: Create a simple game state
import random

class GameState:
    def __init__(self, name):
        self.name = name
    
    def enter(self):
        print(f"Entering {self.name} state")
    
    def handle_input(self):
        pass
    
    def update(self):
        pass
    
    def exit(self):
        print(f"Exiting {self.name} state")


class TreasureState(GameState):
    def __init__(self):
        super().__init__("Treasure")
        self.inventory = []
# It should have these features:
    def handle_input(self):     
        print('\nOptions are:')
        print("1. Look for treasure")
        print("2. Check inventory")
        print("3. Exit game\n")
        
        option = input('Pick a choice: ')
        return option

    def update(self):
        option = self.handle_input()
        if option == "1":
            print("Looking for Treasure!")
            self.find_treasure()
            return "Treasure"
        elif option == "2":
            print('Checking inventory!\n')
            self.check_inventory()
            return "Treasure"
        elif option == '3':
            return 'Exit'
        else:
            print('Invalid option.')
            return "Treasure."

    def find_treasure(self):
        self.treasure = random.randint(0, 2)

        if self.treasure == 0:
            print('No treasure found!!!')
        else:
            print(f'{self.treasure} treasure found!!!')
        
        return self.inventory.append(self.treasure)

    def check_inventory(self):
        for item in self.inventory:
            print(f'{item} gold')


def main():
    pill = TreasureState()
    pill.enter()
    while pill != 'Exit':
        if  pill.update() == '3':
            break

if __name__ == "__main__":
    main()