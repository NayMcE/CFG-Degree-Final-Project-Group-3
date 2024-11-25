import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BOARD_SIZE = 10  # 10x10 board
SQUARE_SIZE = WIDTH // BOARD_SIZE
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (211, 211, 211)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Load images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")  # Replace with your background image file
background_image = pygame.transform.scale(background_image, (WIDTH + SIDE_PANEL_WIDTH, HEIGHT))  # Resize to fit the screen
dice_images = [pygame.image.load(f"dice_{i}.png") for i in range(1, 7)]  # Images for dice 1 to 6
dice_rect = dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))  # Place dice in the center of side panel

# Function to draw the board
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, LIGHT_GRAY, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

            # Add square number (1 to 100)
            num = row * BOARD_SIZE + col + 1
            font = pygame.font.SysFont("Arial", 24)
            text = font.render(str(num), True, BLACK)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to draw the side panel with dice
def draw_side_panel(dice_roll):
    pygame.draw.rect(screen, BLUE, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

# Main game loop
def main():
    running = True
    player_pos = 1  # Player starts at square 1
    while running:
        screen.fill(GREEN)  # Fill the screen with green (for the board background)

        # Draw the background image
        screen.blit(background_image, (0, 0))  # Draw background image

        # Draw board
        draw_board()

        # Draw the side panel and dice
        dice_roll = roll_dice()  # Random dice roll (for demo purposes)
        draw_side_panel(dice_roll)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

# Run the game
main()

# Quit pygame
pygame.quit()
