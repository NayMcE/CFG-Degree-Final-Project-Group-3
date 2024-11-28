import pygame
import random


# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 100

# Colors (for other elements like side panel)
PINK = (252, 116, 183)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Load images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit the screen
dice_images = [pygame.transform.scale(pygame.image.load(f"Images/dice_{i}.jpeg"), (DICE_SIZE, DICE_SIZE)) for i in range(1, 7)]
dice_rect = dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))  # Centered in side panel

# Function to draw the side panel with dice
def draw_side_panel(dice_roll):
    pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

def roll_dice_animation():
    roll_count = 10  # Number of frames in the roll animation
    for _ in range(roll_count):
        # Display random dice face during the animation
        random_face = random.choice(dice_images)
        # screen.fill(WHITE)  # Clear the screen
        screen.blit(random_face, (100, 100))
        pygame.display.update()
        pygame.time.delay(50)  # Short delay to simulate animation

    # Final roll result
    roll_result = random.randint(1, 6)
    # screen.fill(WHITE)
    screen.blit(dice_images[roll_result - 1], (100, 100))
    pygame.display.update()
    return roll_result
# Main game loop
def main():
    running = True
    player_pos = 1  # Player starts at square 1
    while running:
        # Draw the background image (board)
        screen.blit(background_image, (0, 0))  # Draw the board image
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Trigger dice roll animation on space bar press
                    result = roll_dice_animation()


        pygame.display.update()
        # Draw the pink side panel
        draw_side_panel(1)  # You can replace `1` with any dice roll if you want

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()




# Run the game
main()

# Quit pygame
pygame.quit()
