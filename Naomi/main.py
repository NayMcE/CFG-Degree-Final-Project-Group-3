import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 50

# Colors (for other elements like side panel)
PINK = (252, 116, 183)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Load images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")  # Replace with your board image file
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit the screen
dice_images = [pygame.image.load(f"Images/dice_{i}.png") for i in range(1, 7)]  # Images for dice 1 to 6
dice_rect = dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))  # Place dice in the center of side panel

# Function to draw the side panel with dice
def draw_side_panel(dice_roll):
    pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 50, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

# Main game loop
def main():
    running = True
    player_pos = 1  # Player starts at square 1
    while running:
        # Draw the background image (board)
        screen.blit(background_image, (0, 0))  # Draw the board image

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

# Run the game
main()

# Quit pygame
pygame.quit()
