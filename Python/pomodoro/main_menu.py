import pygame
import sys
import os

pygame.init()
# Set up the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main Menu")

# Set up the font
font = pygame.font.SysFont("Arial", 50)

# Set up the button
button_text = font.render("Start Pomodoro", True, (255, 255, 255))
button_rect = button_text.get_rect(center=(400, 300))
def execute_pygame_file(pygame_file):
# Load the Pygame file
    exec(open(pygame_file).read())


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                execute_pygame_file("pomodoro.py") # Open the pomodoro file
# Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(button_text, button_rect)
    pygame.display.update()

