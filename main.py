import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1540
screen_height = 785
#   x1=1919, y1=0, x2=1919, y2=1015
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draw Rectangle")

# Define rectangle parameters
x = 0
y = 600
width = 1535
height = 400

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
