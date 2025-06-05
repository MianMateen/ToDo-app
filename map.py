import pygame

pygame.init()

# Window dimensions
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Window Coordinate Map")
font = pygame.font.Font(None, 24)  # Default font, size 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw grid lines
    for x in range(0, screen_width, 50):
        pygame.draw.line(screen, BLACK, (x, 0), (x, screen_height), 1)
    for y in range(0, screen_height, 50):
        pygame.draw.line(screen, BLACK, (0, y), (screen_width, y), 1)

    # Draw axes
    pygame.draw.line(screen, RED, (0, 0), (screen_width, 0), 3)  # Top edge (X-axis)
    pygame.draw.line(screen, RED, (0, 0), (0, screen_height), 3)  # Left edge (Y-axis)

    # Label key positions
    positions = [
        (0, 0, "(0,0) - Top Left"),
        (screen_width, 0, f"({screen_width},0) - Top Right"),
        (0, screen_height, f"(0,{screen_height}) - Bottom Left"),
        (screen_width, screen_height, f"({screen_width},{screen_height}) - Bottom Right"),
        (screen_width//2, screen_height//2, "Center")
    ]

    for x, y, text in positions:
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x + 10, y + 10))

    # Draw moving point showing coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 5)
    mouse_text = font.render(f"({mouse_x}, {mouse_y})", True, BLACK)
    screen.blit(mouse_text, (mouse_x + 15, mouse_y + 15))

    pygame.display.flip()

pygame.quit()