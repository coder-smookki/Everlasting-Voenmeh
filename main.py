import pygame
import renpy

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the window title
pygame.display.set_caption("My Pygame Window")

# Game loop flag
running = True

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            running = False

    # Drawing (optional - for a blank window, no drawing is needed here)
    # screen.fill((255, 255, 255))  # Fill the background with white

    # Update the display (only needed if drawing is performed)
    # pygame.display.flip()  # or pygame.display.update()

# Quit Pygame
pygame.quit()