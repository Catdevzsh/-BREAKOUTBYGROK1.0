import sys
import math
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Window size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle
paddle_width, paddle_height = 80, 10
paddle_x = (width - paddle_width) / 2
paddle_y = height - 20

# Ball
ball_radius = 10
ball_x, ball_y = (width - ball_radius) / 2, (height - ball_radius) / 2
ball_dx = 3  # Adjusted speed
ball_dy = -3  # Adjusted speed

# Bricks
brick_width, brick_height = 80, 20
brick_rows = 5
brick_cols = 8
brick_spacing = 2
brick_padding = 5

# Create a list of bricks
brick_list = []
for row in range(brick_rows):
    brick_y = 20 + row * (brick_height + brick_spacing)
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_spacing) + brick_padding
        brick_list.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 5

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions
    if ball_y < 0:
        ball_dy *= -1
    elif ball_y > height - ball_radius:
        # Reset the ball
        ball_x, ball_y = (width - ball_radius) / 2, (height - ball_radius) / 2
        ball_dy = -3  # Adjusted speed
    elif ball_x < 0 or ball_x > width - ball_radius:
        ball_dx *= -1

    # Ball and paddle collision
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y + ball_radius < paddle_y + paddle_height:
        ball_dy *= -1

    # Ball and bricks collision
    for brick in brick_list[:]:
        if brick.collidepoint(ball_x, ball_y):
            brick_list.remove(brick)
            ball_dy *= -1
            break

    # Draw the game
    screen.fill(BLACK)

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Draw the bricks
    for brick in brick_list:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.update()

    # Control the frame rate to be 30 FPS
    clock.tick(30)

pygame.quit()
