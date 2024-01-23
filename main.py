import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("@Dev_aladinh production                                                                                                             Shooter Game")

# Set up colors
blue = (0, 0, 255)
pink = (255, 255, 0)
gray = (128, 128, 128)

# Define bullets
bullet_radius = 5
bullet_color = (255, 0, 0)
bullet_speed = 10

# Set up the player's position and dimensions
player_width, player_height = 30, 30
player_x, player_y = width // 2 - player_width // 2, height // 2 - player_height // 2

# Load and resize player image
player_image = pygame.image.load('E:/Denno/DNI Media/Pics album/4D Media/1675580799682.jpg')
player_image = pygame.transform.scale(player_image, (30, 30))

# Load and resize background image
background_image = pygame.image.load('E:/Denno/DNI Media/Pics album/4D Media/v2osk-1Z2niiBPg5A-unsplash (1).jpg')
background_image = pygame.transform.scale(background_image, (width, height))

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - bullet_radius, y - bullet_radius, bullet_radius * 2, bullet_radius * 2)

    def move(self):
        self.rect.y -= bullet_speed

    def draw(self):
        pygame.draw.circle(screen, bullet_color, self.rect.center, bullet_radius)

bullets = []

# Set up the game loop
clock = pygame.time.Clock()
running = True
speed = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            new_bullet = Bullet(player_x + player_width // 2, player_y + player_height // 2)
            bullets.append(new_bullet)

    # Handle player movement
    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    player_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed

    # Restrict player within screen boundaries
    player_x = max(1, min(player_x, width - player_width))
    player_y = max(1, min(player_y, height - player_height))

    # Draw background image
    screen.blit(background_image, (0, 0))

    for bullet in bullets:
        bullet.move()
        bullet.draw()

    bullets = [bullet for bullet in bullets if bullet.rect.y > 0]

    # Draw the player's image
    screen.blit(player_image, (player_x, player_y))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
