import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("GitPod PyGame Works!")

# Colors
BLUE = (100, 150, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 150)

# Game variables
x, y = 50, 50
speed = 5

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Keep player on screen
    x = max(0, min(x, 750))
    y = max(0, min(y, 550))
    
    # Drawing
    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, (x, y, 50, 50))
    pygame.draw.circle(screen, GREEN, (400, 300), 30)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
