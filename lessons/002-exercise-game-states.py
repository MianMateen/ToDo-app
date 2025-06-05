# Exercise: Create a simple game state system for a treasure hunt game

from argparse import Action
from optparse import Option
from typing import override


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


# TODO: Create a MapState class that inherits from GameState
class MapState(GameState):
    def __init__(self):
        super().__init__("Map")
    
    def handle_input(self):
        print("""\nMap menu
                  1. Look for treasure
                  2. Check inventory
                  3. Exit\n""")

        option = input('Pick your choice: ')
        return option
    
    def update(self):
        option = self.handle_input()
        if option == '1':
            print('Looking for treasure!')
            return "Treasure"
        elif option == '2':
            print('Checking inventory!')
            return "Inventory"
        elif option == '3':
            return "Exit"
        else:
            print("Invalid choice. Try again.")
            return "Map"

class TreasureState(GameState):
    def __init__(self):
        super().__init__("Treasure")


    def handle_input(self):
        print('\nTreasure Menu')
        print('1. Pick up treasure')
        print('2. Back to Map')

        option = input('Pick an option: ')
        return option

    def update(self):
        option = self.handle_input()

        if option == '1':
            print('Picking up treasure!!!')
            return 'Treasure'
        elif option == '2':
            print("Going back to map")
            return 'Map'
        else:
            print("Invalid choice. Try again.")
            return "Treasure"

class GameStateManager:
    def __init__(self):
        self.states = {
            'Map': MapState(),
            'Treasure': TreasureState(),
            'Inventory': None,
            'Exit': None,
        }

        self.current_state = 'Map'

    def change_state(self, new_state):
        if new_state in self.states:
            if self.states[self.current_state]:
                self.states[self.current_state].exit()
            self.current_state = new_state
            self.states[self.current_state].enter()
        else:
            print(f'{new_state} doesnt exit.')
    
    def run(self):
        if self.current_state != 'Exit':
            next_state = self.states[self.current_state].update()
            if next_state != self.current_state:
                self.change_state(next_state)


def main():
    game = GameStateManager()
    game.run()

if __name__ == "__main__":
    main()