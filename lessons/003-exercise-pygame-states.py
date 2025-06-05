from typing import override
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class GameState:
    def __init__(self, name):
        self.name = name
    
    def handle_events(self, events):
        pass
    
    def update(self):
        pass
    
    def draw(self, screen):
        pass
class MenuState(GameState):
    def __init__(self):
        super().__init__("Menu")

    def handle_events(self, events):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type


# The menu should show:
# 1. Start Game (goes to Game state)
# 2. Instructions (goes to Instructions state)
# 3. Exit (exits the game)

# TODO: Create a Game state that inherits from GameState
# The game should show:
# 1. Look for Treasure
# 2. Check Inventory
# 3. Back to Menu

# TODO: Create an Instructions state that inherits from GameState
# The instructions should show:
# 1. Back to Menu

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("State-Based Treasure Game")
        self.clock = pygame.time.Clock()
        self.current_state = "Menu"  # Start in Menu state
        
        # Create all states
        self.states = {
            "Menu": MenuState(),
            "Game": GameState(),
            "Instructions": GameState()
        }
    
    def run(self):
        while True:
            # Get events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            # Handle current state
            self.states[self.current_state].handle_events(events)
            self.states[self.current_state].update()
            
            # Draw everything
            self.screen.fill(BLACK)
            self.states[self.current_state].draw(self.screen)
            pygame.display.flip()
            
            # Limit to 60 FPS
            self.clock.tick(60)

def main():
    game = GameWindow()
    game.run()

if __name__ == "__main__":
    main()