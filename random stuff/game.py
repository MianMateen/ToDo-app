import pygame
import sys
import math
import random
from pygame import gfxdraw

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battlefield Tactics Card Game - Combat Version")

# Colors
BACKGROUND = (40, 44, 52)
GRID_COLOR = (80, 80, 100)
CARD_COLORS = {
    'light_inf': (126, 182, 255),
    'heavy_inf': (80, 120, 200),
    'cavalry': (220, 120, 100),
    'mage': (200, 100, 220),
    'healer': (100, 220, 120),
    'knight': (220, 180, 80),
    'champion': (240, 200, 40),
    'special': (180, 100, 220)
}
TEXT_COLOR = (240, 240, 240)
HIGHLIGHT = (255, 255, 0)
CONTROL_PANEL = (60, 60, 80)
BUTTON_COLOR = (80, 130, 220)
BUTTON_HOVER = (100, 150, 240)
ATTACK_HIGHLIGHT = (255, 50, 50)

# Game constants
GRID_SIZE = 70
GRID_WIDTH = 10
GRID_HEIGHT = 8
GRID_OFFSET_X = (WIDTH - GRID_WIDTH * GRID_SIZE) // 2
GRID_OFFSET_Y = 50

# Fonts
font_small = pygame.font.SysFont(None, 20)
font_medium = pygame.font.SysFont(None, 24)
font_large = pygame.font.SysFont(None, 32)

# Advantage multipliers
ADVANTAGE_MULTIPLIER = 1.5  # 50% bonus damage
DISADVANTAGE_MULTIPLIER = 0.5  # 50% reduced damage

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.hovered = False
        
    def draw(self, surface):
        color = BUTTON_HOVER if self.hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, 0, 10)
        pygame.draw.rect(surface, (120, 160, 240), self.rect, 2, 10)
        
        text_surf = font_medium.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered
        
    def check_click(self, pos):
        return self.rect.collidepoint(pos)

class Card:
    def __init__(self, x, y, card_type, value, suit, is_player=True):
        self.x = x
        self.y = y
        self.type = card_type
        self.value = value
        self.suit = suit
        self.is_player = is_player
        self.width = GRID_SIZE - 4
        self.height = GRID_SIZE - 4
        self.selected = False
        self.health = 100
        self.attack = 50
        self.moving = False
        self.target_x = x
        self.target_y = y
        self.speed = 2
        self.has_moved = False
        self.has_attacked = False
        self.attack_target = None
        self.being_attacked = False
        
        # Set properties based on card type
        if card_type == "light_inf":
            self.color = CARD_COLORS['light_inf']
            self.speed = 3
            self.attack = 40
            self.advantages = ["heavy_inf", "mage"]
        elif card_type == "heavy_inf":
            self.color = CARD_COLORS['heavy_inf']
            self.health = 150
            self.speed = 1.5
            self.attack = 60
            self.advantages = ["cavalry"]
        elif card_type == "cavalry":
            self.color = CARD_COLORS['cavalry']
            self.attack = 75
            self.speed = 4
            self.advantages = ["light_inf", "mage"]
        elif card_type == "mage":
            self.color = CARD_COLORS['mage']
            self.health = 70
            self.attack = 90
            self.advantages = ["heavy_inf", "cavalry", "knight", "champion"]
        elif card_type == "healer":
            self.color = CARD_COLORS['healer']
            self.attack = 30
            self.health = 120
            self.advantages = []  # Healers don't attack
        elif card_type == "knight":
            self.color = CARD_COLORS['knight']
            self.health = 160
            self.attack = 80
            self.advantages = ["light_inf", "heavy_inf", "cavalry"]
        elif card_type == "champion":
            self.color = CARD_COLORS['champion']
            self.health = 200
            self.attack = 85
            self.advantages = ["light_inf", "heavy_inf", "cavalry", "knight"]
        else:  # special
            self.color = CARD_COLORS['special']
            self.health = 250
            self.attack = 100
            self.advantages = ["light_inf", "heavy_inf", "cavalry", "mage", "knight", "champion"]
            
    def draw(self, surface):
        # Draw card background
        color = self.color
        if self.selected:
            # Highlight selected card
            pygame.draw.rect(surface, HIGHLIGHT, 
                            (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 8)
        
        if self.being_attacked:
            # Highlight card being attacked
            pygame.draw.rect(surface, ATTACK_HIGHLIGHT, 
                            (self.x - 3, self.y - 3, self.width + 6, self.height + 6), 3, 8)
        
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height), 0, 8)
        
        # Draw card type text
        text = font_small.render(self.type.replace('_', ' '), True, TEXT_COLOR)
        surface.blit(text, (self.x + self.width//2 - text.get_width()//2, self.y + 5))
        
        # Draw stats
        stats = f"HP: {self.health} ATK: {self.attack}"
        text = font_small.render(stats, True, TEXT_COLOR)
        surface.blit(text, (self.x + self.width//2 - text.get_width()//2, self.y + self.height - 20))
        
        # Draw suit and value
        text = font_medium.render(f"{self.value}", True, TEXT_COLOR)
        surface.blit(text, (self.x + self.width//2 - text.get_width()//2, self.y + self.height//2 - 10))
        
        # Draw health bar
        max_health = self.get_max_health()
        health_width = (self.width - 10) * (self.health / max_health) if max_health > 0 else 0
        pygame.draw.rect(surface, (50, 50, 50), (self.x + 5, self.y + self.height - 10, self.width - 10, 5), 0, 3)
        pygame.draw.rect(surface, (0, 255, 0), (self.x + 5, self.y + self.height - 10, health_width, 5), 0, 3)
        
        # Draw movement and attack status
        if self.has_moved:
            pygame.draw.circle(surface, (255, 100, 100), (self.x + 10, self.y + 10), 5)
        if self.has_attacked:
            pygame.draw.circle(surface, (255, 200, 100), (self.x + 25, self.y + 10), 5)
    
    def get_max_health(self):
        if self.type == "heavy_inf":
            return 150
        elif self.type == "knight":
            return 160
        elif self.type == "champion":
            return 200
        elif self.type == "mage":
            return 70
        elif self.type == "healer":
            return 120
        elif self.type == "special":
            return 250
        return 100
    
    def move_toward_target(self):
        if self.moving:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance < self.speed:
                self.x = self.target_x
                self.y = self.target_y
                self.moving = False
                self.has_moved = True
            else:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed
    
    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y
        self.moving = True
    
    def contains_point(self, point):
        return (self.x <= point[0] <= self.x + self.width and
                self.y <= point[1] <= self.y + self.height)
                
    def reset_turn(self):
        self.has_moved = False
        self.has_attacked = False
        self.attack_target = None
        self.being_attacked = False
    
    def get_grid_position(self):
        grid_x = int((self.x - GRID_OFFSET_X + GRID_SIZE/2) // GRID_SIZE)
        grid_y = int((self.y - GRID_OFFSET_Y + GRID_SIZE/2) // GRID_SIZE)
        return grid_x, grid_y
    
    def is_adjacent(self, other_card):
        x1, y1 = self.get_grid_position()
        x2, y2 = other_card.get_grid_position()
        
        # Check if cards are adjacent (including diagonally)
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    
    def calculate_damage(self, target):
        base_damage = self.attack
        
        # Check for advantage/disadvantage
        if target.type in self.advantages:
            damage = base_damage * ADVANTAGE_MULTIPLIER
            return int(damage), "advantage"
        elif self.type in target.advantages:
            damage = base_damage * DISADVANTAGE_MULTIPLIER
            return int(damage), "disadvantage"
        else:
            return base_damage, "neutral"
    
    def attack_unit(self, target):
        if self.has_attacked:
            return False, "Already attacked this turn"
        
        if not self.is_adjacent(target):
            return False, "Target not adjacent"
        
        if self.is_player == target.is_player:
            return False, "Cannot attack friendly units"
        
        damage, status = self.calculate_damage(target)
        target.health -= damage
        
        # Counter-attack (if target can attack back and hasn't attacked yet)
        if target.health > 0 and target.type != "healer" and not target.has_attacked:
            counter_damage, counter_status = target.calculate_damage(self)
            self.health -= counter_damage
            target.has_attacked = True
        
        self.has_attacked = True
        return True, f"Attacked for {damage} damage ({status})"

class Game:
    def __init__(self):
        self.cards = []
        self.selected_card = None
        self.players_turn = True
        self.turn_timer = 0
        self.turn_time = 30  # seconds per turn
        self.message = "Place your units on the grid"
        self.game_state = "setup"  # setup, battle, game_over
        self.buttons = []
        self.initialize_cards()
        self.create_buttons()
        self.ai_thinking = False
        self.ai_timer = 0
        self.attack_mode = False
        
    def initialize_cards(self):
        # Create a standard deck of cards with different types
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        types = [
            ('light_inf', [2, 3, 4]),
            ('heavy_inf', [5, 6, 7]),
            ('cavalry', [9, 10]),
            ('mage', ['J']),
            ('healer', ['Q']),
            ('knight', ['K']),
            ('champion', ['A'])
        ]
        
        # Create player cards
        for suit in suits[:2]:  # First two suits for player
            for card_type, values in types:
                for value in values:
                    self.cards.append(Card(
                        50 + len([c for c in self.cards if c.is_player]) * 30,  # Initial position off-grid
                        500,
                        card_type,
                        str(value),
                        suit,
                        True
                    ))
        
        # Create AI cards (positioned off-grid at the top)
        for suit in suits[2:]:  # Last two suits for AI
            for card_type, values in types:
                for value in values:
                    self.cards.append(Card(
                        50 + len([c for c in self.cards if not c.is_player]) * 30,
                        50,
                        card_type,
                        str(value),
                        suit,
                        False
                    ))
    
    def create_buttons(self):
        # Create action buttons
        self.buttons = [
            Button(WIDTH - 180, HEIGHT - 80, 160, 60, "End Turn", self.end_turn),
            Button(20, HEIGHT - 80, 160, 60, "Combine", self.combine_selected),
            Button(WIDTH // 2 - 80, HEIGHT - 80, 160, 60, "Start Battle", self.start_battle),
            Button(WIDTH // 2 - 240, HEIGHT - 80, 160, 60, "Attack", self.toggle_attack_mode)
        ]
    
    def draw(self, surface):
        # Draw grid background
        pygame.draw.rect(surface, (50, 50, 60), 
                        (GRID_OFFSET_X - 10, GRID_OFFSET_Y - 10, 
                         GRID_WIDTH * GRID_SIZE + 20, GRID_HEIGHT * GRID_SIZE + 20), 0, 10)
        
        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                rect = pygame.Rect(
                    GRID_OFFSET_X + x * GRID_SIZE,
                    GRID_OFFSET_Y + y * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE
                )
                pygame.draw.rect(surface, GRID_COLOR, rect, 1)
                
                # Draw row labels (player vs AI areas)
                if y == 0:
                    text = font_small.render("AI Territory", True, (200, 100, 100))
                    surface.blit(text, (10, GRID_OFFSET_Y + y * GRID_SIZE + GRID_SIZE // 3))
                elif y == GRID_HEIGHT - 1:
                    text = font_small.render("Player Territory", True, (100, 200, 100))
                    surface.blit(text, (10, GRID_OFFSET_Y + y * GRID_SIZE + GRID_SIZE // 3))
        
        # Draw cards
        for card in self.cards:
            card.draw(surface)
        
        # Draw control panel
        pygame.draw.rect(surface, CONTROL_PANEL, (0, HEIGHT - 100, WIDTH, 100), 0, 15)
        
        # Draw game info
        text = font_large.render(self.message, True, TEXT_COLOR)
        surface.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 90))
        
        # Draw turn timer
        if self.game_state == "battle":
            timer_text = f"Time left: {int(self.turn_timer)}s"
            text = font_medium.render(timer_text, True, TEXT_COLOR)
            surface.blit(text, (WIDTH - 150, 10))
            
            turn_text = "Your Turn" if self.players_turn else "AI's Turn"
            text = font_medium.render(turn_text, True, (100, 200, 100) if self.players_turn else (200, 100, 100))
            surface.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))
            
            # Draw attack mode status
            if self.attack_mode:
                mode_text = "ATTACK MODE: Select target"
                text = font_medium.render(mode_text, True, (255, 100, 100))
                surface.blit(text, (20, 40))
        
        # Draw buttons
        for button in self.buttons:
            button.draw(surface)
            
        # Draw instructions
        if self.game_state == "setup":
            instructions = [
                "Click to select a unit, click again to place on grid",
                "Use Combine button to merge units of same type",
                "Place units in your territory (bottom rows)",
                "Press Start Battle when ready"
            ]
            
            for i, instruction in enumerate(instructions):
                text = font_small.render(instruction, True, (180, 180, 200))
                surface.blit(text, (20, HEIGHT - 200 - i*25))
        else:
            instructions = [
                "Click to select a unit, click on grid to move",
                "Use Combine button to merge selected units",
                "Press Attack button, then select enemy to attack",
                "Press End Turn when finished"
            ]
            
            for i, instruction in enumerate(instructions):
                text = font_small.render(instruction, True, (180, 180, 200))
                surface.blit(text, (20, HEIGHT - 200 - i*25))
                
        # Draw AI thinking indicator
        if self.ai_thinking:
            text = font_medium.render("AI is thinking...", True, (200, 150, 100))
            surface.blit(text, (WIDTH // 2 - text.get_width() // 2, 40))
    
    def update(self, dt):
        # Update cards
        for card in self.cards:
            card.move_toward_target()
        
        # Remove dead cards
        self.cards = [card for card in self.cards if card.health > 0]
        
        # Check win conditions
        player_units = sum(1 for card in self.cards if card.is_player)
        ai_units = sum(1 for card in self.cards if not card.is_player)
        
        if self.game_state == "battle":
            if player_units == 0:
                self.game_state = "game_over"
                self.message = "Game Over - AI Wins!"
            elif ai_units == 0:
                self.game_state = "game_over"
                self.message = "Victory - You Win!"
        
        # Update turn timer
        if self.game_state == "battle" and self.players_turn:
            self.turn_timer -= dt
            if self.turn_timer <= 0:
                self.end_turn()
                
        # Update AI thinking timer
        if self.ai_thinking:
            self.ai_timer -= dt
            if self.ai_timer <= 0:
                self.ai_thinking = False
                self.ai_move()
    
    def handle_click(self, pos, right_click=False):
        # Check if a button was clicked FIRST
        for button in self.buttons:
            if button.check_click(pos):
                if button.action:
                    button.action()
                return
                
        # Check if a card was clicked
        for card in self.cards:
            if card.contains_point(pos):
                if self.attack_mode and self.selected_card and self.selected_card != card:
                    # Attack mode - target selected
                    success, message = self.selected_card.attack_unit(card)
                    self.message = message
                    self.attack_mode = False
                    card.being_attacked = True
                    pygame.time.set_timer(pygame.USEREVENT, 1000)  # Reset attack highlight after 1 second
                    return
                
                if right_click:
                    # Try to combine with selected card
                    if self.selected_card and self.selected_card != card:
                        self.combine_cards(self.selected_card, card)
                    return
                
                if self.selected_card == card:
                    # Deselect card
                    self.selected_card.selected = False
                    self.selected_card = None
                    self.attack_mode = False
                else:
                    # Select this card
                    if self.selected_card:
                        self.selected_card.selected = False
                    self.selected_card = card
                    card.selected = True
                    self.attack_mode = False
                return
        
        # If a card is selected and we clicked on grid, move it
        if self.selected_card and self.selected_card.is_player and (self.game_state == "battle" or self.game_state == "setup"):
            grid_x = (pos[0] - GRID_OFFSET_X) // GRID_SIZE
            grid_y = (pos[1] - GRID_OFFSET_Y) // GRID_SIZE
            
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                # Check if position is valid (on player's side during setup)
                if self.game_state == "setup" and grid_y < GRID_HEIGHT // 2:
                    self.message = "Can only place units in your territory!"
                    return
                
                # Check if there's already a card at this position
                for card in self.cards:
                    card_grid_x = (card.x - GRID_OFFSET_X + GRID_SIZE/2) // GRID_SIZE
                    card_grid_y = (card.y - GRID_OFFSET_Y + GRID_SIZE/2) // GRID_SIZE
                    if card_grid_x == grid_x and card_grid_y == grid_y and card != self.selected_card:
                        if right_click:
                            self.combine_cards(self.selected_card, card)
                        else:
                            self.message = "Position already occupied!"
                        return
                
                # Move the card
                self.selected_card.set_target(
                    GRID_OFFSET_X + grid_x * GRID_SIZE + 2,
                    GRID_OFFSET_Y + grid_y * GRID_SIZE + 2
                )
                self.selected_card.selected = False
                self.selected_card = None
                self.message = "Unit moved"
                self.attack_mode = False
    
    def combine_cards(self, card1, card2):
        # Check if cards can be combined (same type and same player)
        if (card1.type == card2.type and card1.is_player == card2.is_player):
            # Combine stats
            card1.health = min(card1.get_max_health(), card1.health + card2.health // 2)
            card1.attack += card2.attack // 4
            
            # Remove card2
            self.cards.remove(card2)
            self.message = f"Combined {card1.type} units!"
        else:
            self.message = "Can only combine units of the same type and same side!"
    
    def combine_selected(self):
        if self.selected_card:
            # Find another card of the same type to combine with
            for card in self.cards:
                if (card != self.selected_card and card.type == self.selected_card.type and 
                    card.is_player == self.selected_card.is_player):
                    self.combine_cards(self.selected_card, card)
                    return
            
            self.message = "No similar unit to combine with!"
        else:
            self.message = "Select a unit first!"
    
    def toggle_attack_mode(self):
        if self.game_state == "battle" and self.selected_card and self.selected_card.is_player:
            if self.selected_card.has_attacked:
                self.message = "This unit has already attacked this turn"
                return
                
            self.attack_mode = not self.attack_mode
            if self.attack_mode:
                self.message = "Attack mode: Select an enemy to attack"
            else:
                self.message = "Attack mode cancelled"
    
    def end_turn(self):
        if self.players_turn and self.game_state == "battle":
            self.players_turn = False
            self.turn_timer = self.turn_time
            self.message = "AI's turn"
            self.attack_mode = False
            
            # Reset player units
            for card in self.cards:
                if card.is_player:
                    card.reset_turn()
            
            # Start AI thinking with a delay
            self.ai_thinking = True
            self.ai_timer = 1.5  # AI will move after 1.5 seconds
    
    def ai_move(self):
        # Simple AI: move random units toward player territory and attack
        ai_units = [card for card in self.cards if not card.is_player and not card.has_moved]
        player_units = [card for card in self.cards if card.is_player]
        
        if not ai_units:
            # AI has no units to move, end turn
            self.players_turn = True
            self.turn_timer = self.turn_time
            self.message = "Your turn"
            
            # Reset AI units
            for card in self.cards:
                if not card.is_player:
                    card.reset_turn()
            return
            
        # Move up to 3 AI units per turn
        for unit in random.sample(ai_units, min(3, len(ai_units))):
            grid_x, grid_y = unit.get_grid_position()
            
            # Try to attack if adjacent to player unit
            for player_unit in player_units:
                if unit.is_adjacent(player_unit) and not unit.has_attacked:
                    success, message = unit.attack_unit(player_unit)
                    if success:
                        self.message = f"AI {unit.type} attacked your {player_unit.type}"
                        player_unit.being_attacked = True
                        pygame.time.set_timer(pygame.USEREVENT, 1000)  # Reset attack highlight after 1 second
                    break
            
            # If didn't attack, try to move toward player territory
            if not unit.has_attacked and grid_y < GRID_HEIGHT - 1:
                # Try to move toward nearest player unit
                nearest_player = None
                min_dist = float('inf')
                
                for p_unit in player_units:
                    p_grid_x, p_grid_y = p_unit.get_grid_position()
                    dist = abs(p_grid_x - grid_x) + abs(p_grid_y - grid_y)
                    
                    if dist < min_dist:
                        min_dist = dist
                        nearest_player = p_unit
                
                if nearest_player:
                    p_grid_x, p_grid_y = nearest_player.get_grid_position()
                    
                    # Calculate movement direction
                    dx = 0
                    if p_grid_x > grid_x:
                        dx = 1
                    elif p_grid_x < grid_x:
                        dx = -1
                    
                    dy = 0
                    if p_grid_y > grid_y:
                        dy = 1
                    
                    new_x = max(0, min(GRID_WIDTH - 1, grid_x + dx))
                    new_y = max(0, min(GRID_HEIGHT - 1, grid_y + dy))
                    
                    # Check if position is free
                    position_free = True
                    for other in self.cards:
                        other_x, other_y = other.get_grid_position()
                        if other_x == new_x and other_y == new_y and other != unit:
                            position_free = False
                            break
                    
                    if position_free:
                        unit.set_target(
                            GRID_OFFSET_X + new_x * GRID_SIZE + 2,
                            GRID_OFFSET_Y + new_y * GRID_SIZE + 2
                        )
                        unit.has_moved = True
        
        # After AI move, end AI turn
        self.players_turn = True
        self.turn_timer = self.turn_time
        self.message = "Your turn"
        
        # Reset AI units for next turn
        for card in self.cards:
            if not card.is_player:
                card.reset_turn()
    
    def start_battle(self):
        if self.game_state == "setup":
            self.game_state = "battle"
            self.players_turn = True
            self.turn_timer = self.turn_time
            self.message = "Battle started! It's your turn."

# Create game instance
game = Game()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    
    # Get mouse position for button hover effect
    mouse_pos = pygame.mouse.get_pos()
    for button in game.buttons:
        button.check_hover(mouse_pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                game.handle_click(event.pos)
            elif event.button == 3:  # Right click
                game.handle_click(event.pos, True)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.game_state == "setup":
                    game.start_battle()
                else:
                    game.end_turn()
        elif event.type == pygame.USEREVENT:
            # Reset attack highlights
            for card in game.cards:
                card.being_attacked = False
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Remove timer
    
    # Update game state
    game.update(dt)
    
    # Draw everything
    screen.fill(BACKGROUND)
    game.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()