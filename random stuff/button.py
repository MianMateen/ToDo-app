import pygame

pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test game with pygame')
clock = pygame.time.Clock()


class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def draw_text(self):
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def clear_text(self):
        self.text = " "
        return self.text


def main():
    running = True
    button = Button(300, 400, 100, 30, RED, "Click me")
    button2 = Button(300, 350, 100, 30, BLUE, "Don't click")
    
    screen.fill(WHITE)
    screen_color = WHITE

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    screen_color = RED
                    screen.fill(screen_color)
                    button.clear_text()
                
                elif button2.is_clicked(event.pos):
                    screen_color = BLUE
                    screen.fill(screen_color)
                    button2.clear_text()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:    # Then check which key
                    screen_color = WHITE
                    screen.fill(screen_color)

            if screen_color == WHITE and button.text == " ":
                button.text = "click me"
            elif screen_color == WHITE and button2.text == " ":
                button2.text = "Don't click"

        if not screen_color == BLUE:
            button.draw()      # Draws the red rectangle
            button.draw_text()      # Displays the text for the red rectangle
        elif screen_color == BLUE:
            button2.clear_text()

        if not screen_color == RED:
            button2.draw()      # Draws the blue rectangle
            button2.draw_text()      # Displays the text for the blue rectangle
        pygame.display.flip()   # Updates the screen
        clock.tick(60)     # caps the screen to 60 fps

if __name__  == "__main__":
    main()
    pygame.quit()