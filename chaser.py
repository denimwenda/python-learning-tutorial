import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
TARGET_SIZE = 30
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaser Game")

# Create player and target
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)
target = pygame.Rect(random.randint(0, WIDTH - TARGET_SIZE), random.randint(0, HEIGHT - TARGET_SIZE), TARGET_SIZE, TARGET_SIZE)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Keep the player within the screen bounds
    player.x = max(0, min(player.x, WIDTH - PLAYER_SIZE))
    player.y = max(0, min(player.y, HEIGHT - PLAYER_SIZE))

    # Check if player has caught the target
    if player.colliderect(target):
        target.x = random.randint(0, WIDTH - TARGET_SIZE)
        target.y = random.randint(0, HEIGHT - TARGET_SIZE)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player and target
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, target)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
