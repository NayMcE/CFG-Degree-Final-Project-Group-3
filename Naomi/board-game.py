import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Board Game")

# Load the background image
background = pygame.image.load("Alice-In-Wonderland_Board_Game.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)

# Load a player piece (token)
player_token = pygame.Surface((50, 50))
player_token.fill((255, 0, 0))  # Red square as a placeholder for the token

# Initial position of the token
player_pos = [100, 100]

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= 5  # Move up
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5  # Move down
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Move right

    # Ensure token stays within screen boundaries
    player_pos[0] = max(0, min(SCREEN_WIDTH - 50, player_pos[0]))
    player_pos[1] = max(0, min(SCREEN_HEIGHT - 50, player_pos[1]))

    # Draw everything
    screen.blit(background, (0, 0))  # Draw the background
    screen.blit(player_token, player_pos)  # Draw the player token

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()