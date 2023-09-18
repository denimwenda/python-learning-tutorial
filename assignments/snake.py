import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (0, -1)  # Start moving up
snake_growth = False

# Initialize Food
food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
        random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

# Game Over Flag
game_over = False

# Main Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move Snake
    new_head = (snake[0][0] + snake_direction[0] * SNAKE_SIZE,
                snake[0][1] + snake_direction[1] * SNAKE_SIZE)
    snake.insert(0, new_head)

    # Check for Collision with Food
    if snake[0] == food:
        snake_growth = True
        food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

    # Check for Collision with Walls or Self
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
        game_over = True

    # Remove Tail if not Growing
    if not snake_growth:
        snake.pop()

    # Draw Screen
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, WHITE, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.update()

    # Control Game Speed
    time.sleep(1 / SNAKE_SPEED)

# Quit Pygame
pygame.quit()