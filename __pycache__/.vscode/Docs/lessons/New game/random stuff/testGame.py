import pygame
import sys
import random

# Initialize
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OpenFront: GUI RTS")
clock = pygame.time.Clock()

# Map
TILE_SIZE = 40
MAP_WIDTH, MAP_HEIGHT = 30, 18
FPS = 60
camera_x, camera_y = 0, 0

# Colors
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Units
units = []

class Unit:
    def __init__(self, x, y, team):
        self.x, self.y = x, y
        self.team = team
        self.health = 100
        self.max_health = 100
        self.selected = False
        self.target = None
        self.speed = 1 if team == "player" else 0.5

    def draw(self, surface):
        color = BLUE if self.team == "player" else RED
        pygame.draw.rect(surface, color, self.rect())
        if self.selected:
            pygame.draw.rect(surface, WHITE, self.rect(), 2)

        # Draw health bar
        hp_width = TILE_SIZE * (self.health / self.max_health)
        pygame.draw.rect(surface, RED, (self.x * TILE_SIZE - camera_x, self.y * TILE_SIZE - camera_y - 5, TILE_SIZE, 4))
        pygame.draw.rect(surface, GREEN, (self.x * TILE_SIZE - camera_x, self.y * TILE_SIZE - camera_y - 5, hp_width, 4))

    def rect(self):
        return pygame.Rect(self.x * TILE_SIZE - camera_x, self.y * TILE_SIZE - camera_y, TILE_SIZE, TILE_SIZE)

    def update(self):
        if self.target:
            tx, ty = self.target
            if abs(tx - self.x) > 0.1 or abs(ty - self.y) > 0.1:
                dx = tx - self.x
                dy = ty - self.y
                dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist
            else:
                self.target = None

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0 and self in units:
            units.remove(self)

# Map generator
def generate_map():
    return [[GREEN if (x + y) % 2 == 0 else DARK_GREEN for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]

game_map = generate_map()

# GUI elements
font = pygame.font.SysFont("Arial", 18)

def draw_top_bar():
    pygame.draw.rect(screen, GRAY, (0, 0, SCREEN_WIDTH, 40))
    text = font.render("Gold: 200  |  Units: " + str(len(units)), True, WHITE)
    screen.blit(text, (10, 10))

def draw_minimap():
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 180, 170, 170))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 180, 170, 170), 2)

def draw_unit_panel():
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - 200, 40, 200, SCREEN_HEIGHT - 220))
    selected = [u for u in units if u.selected]
    if selected:
        name = "Soldier" if selected[0].team == "player" else "Enemy"
        hp = selected[0].health
        info = font.render(f"{name} | HP: {int(hp)}", True, WHITE)
        screen.blit(info, (SCREEN_WIDTH - 190, 60))

def draw_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            color = game_map[y][x]
            rect = pygame.Rect(x * TILE_SIZE - camera_x, y * TILE_SIZE - camera_y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def handle_input():
    global camera_x, camera_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: camera_x -= 10
    if keys[pygame.K_d]: camera_x += 10
    if keys[pygame.K_w]: camera_y -= 10
    if keys[pygame.K_s]: camera_y += 10

def select_unit(mouse_pos):
    mx, my = mouse_pos
    map_x = (mx + camera_x) // TILE_SIZE
    map_y = (my + camera_y) // TILE_SIZE
    for unit in units:
        unit.selected = False
        if int(unit.x) == map_x and int(unit.y) == map_y and unit.team == "player":
            unit.selected = True

def right_click_command(mouse_pos):
    mx, my = mouse_pos
    tx = (mx + camera_x) // TILE_SIZE
    ty = (my + camera_y) // TILE_SIZE
    for unit in units:
        if unit.selected:
            unit.target = (tx, ty)

def spawn_units():
    units.append(Unit(5, 5, "player"))
    for _ in range(3):
        x, y = random.randint(10, 25), random.randint(5, 15)
        units.append(Unit(x, y, "enemy"))

def update_warfare():
    for unit in units:
        if unit.team == "player":
            for enemy in [u for u in units if u.team == "enemy"]:
                if abs(enemy.x - unit.x) < 1 and abs(enemy.y - unit.y) < 1:
                    enemy.take_damage(0.5)
        elif unit.team == "enemy":
            for player in [u for u in units if u.team == "player"]:
                if abs(player.x - unit.x) < 1 and abs(player.y - unit.y) < 1:
                    player.take_damage(0.2)

# Main loop
def main():
    spawn_units()
    running = True
    while running:
        screen.fill((0, 0, 0))
        handle_input()
        draw_map()

        for unit in units:
            unit.update()
            unit.draw(screen)

        update_warfare()
        draw_top_bar()
        draw_unit_panel()
        draw_minimap()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: select_unit(event.pos)
                elif event.button == 3: right_click_command(event.pos)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()