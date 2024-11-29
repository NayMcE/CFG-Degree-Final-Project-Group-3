import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 100
WHITE = (255, 255, 255)
PINK = (252, 116, 183)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Load images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
dice_images = [pygame.transform.scale(pygame.image.load(f"Images/dice_{i}.jpeg"), (DICE_SIZE, DICE_SIZE))
    for i in range(1, 7)]
dice_rect = dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))

# Function to draw the side panel with dice
def draw_side_panel(dice_roll):
    pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

# Function to animate dice roll
def roll_dice_animation():
    roll_count = 10  # Number of frames in the roll animation
    for i in range(roll_count):
        # Display random dice face during the animation
        random_face = random.choice(dice_images)
        # Clear the dice animation area
        screen.fill(WHITE, (850, 250, DICE_SIZE, DICE_SIZE))
        screen.blit(random_face, (850,250)) # Animation position
        # draw_side_panel(3)  # Keep the side panel visible
        pygame.display.update()
        pygame.time.delay(50) # Short delay to simulate animation

    # Final roll result
    roll_result = random.randint(1, 6)
    screen.fill(WHITE, (800, 100, DICE_SIZE, DICE_SIZE))
    screen.blit(dice_images[roll_result - 1], (800, 100))
    draw_side_panel(roll_result)  # Update side panel with final roll
    pygame.display.update()
    return roll_result

class BoardGame:
    def __init__(self):
        self.ladders = {}
        self.rabbithole = {}
        self.players = {1:alice, 2: white_rabbit}
        self.positions = {1:0}
# Main game loop
def main():
    running = True
    dice_roll = 1  # Default dice roll to show on the side panel
    while running:
        # Draw the board and side panel
        screen.blit(background_image, (0, 0))
        draw_side_panel(dice_roll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Trigger dice roll animation on space bar press
                    dice_roll = roll_dice_animation()

        pygame.display.update()

if __name__ == "__main__":
# Run the game
    main()

# Quit pygame
    pygame.quit()
