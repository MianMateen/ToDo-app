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


class MenuState(GameState):
    def __init__(self):
        super().__init__("Menu")
    
    def handle_input(self):
        print("\nMenu Options:")
        print("1. Start Battle")
        print("2. View Characters")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        return choice
    
    def update(self):
        choice = self.handle_input()
        
        if choice == "1":
            return "Battle"
        elif choice == "2":
            return "CharacterSelect"
        elif choice == "3":
            return "Exit"
        else:
            print("Invalid choice. Try again.")
            return "Menu"


class BattleState(GameState):
    def __init__(self):
        super().__init__("Battle")
    
    def handle_input(self):
        print("\nBattle Options:")
        print("1. Attack")
        print("2. Use Special")
        print("3. Back to Menu")
        
        choice = input("Enter your choice: ")
        return choice
    
    def update(self):
        choice = self.handle_input()
        
        if choice == "1":
            print("Attacking!")
            return "Battle"
        elif choice == "2":
            print("Using special ability!")
            return "Battle"
        elif choice == "3":
            return "Menu"
        else:
            print("Invalid choice. Try again.")
            return "Battle"


class GameStateManager:
    def __init__(self):
        self.states = {
            "Menu": MenuState(),
            "Battle": BattleState(),
            "CharacterSelect": None,  # We'll implement this later
            "Exit": None
        }
        self.current_state = "Menu"
    
    def change_state(self, new_state):
        if new_state in self.states:
            if self.current_state:
                self.states[self.current_state].exit()
            self.current_state = new_state
            self.states[self.current_state].enter()
        else:
            print(f"Error: State {new_state} does not exist")
    
    def run(self):
        while self.current_state != "Exit":
            next_state = self.states[self.current_state].update()
            if next_state != self.current_state:
                self.change_state(next_state)


def main():
    game = GameStateManager()
    game.run()


if __name__ == "__main__":
    main()