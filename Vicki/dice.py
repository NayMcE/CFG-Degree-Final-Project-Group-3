import pygame
import random


# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Roll the Dice")

# Load dice images (ensure these images are in the same folder as your script)
# Load and resize dice images
dice_images = [
    pygame.transform.scale(pygame.image.load(f'dice{i}.png'), (100, 100)) for i in range(1, 7)
]


# Define some colors
WHITE = (255, 255, 255)


# Function to simulate dice roll with animation
def roll_dice_animation():
    roll_count = 10  # Number of frames in the roll animation
    for _ in range(roll_count):
        # Display random dice face during the animation
        random_face = random.choice(dice_images)
        screen.fill(WHITE)  # Clear the screen
        screen.blit(random_face, (100, 100))
        pygame.display.update()
        pygame.time.delay(50)  # Short delay to simulate animation

    # Final roll result
    roll_result = random.randint(1, 6)
    screen.fill(WHITE)
    screen.blit(dice_images[roll_result - 1], (100, 100))
    pygame.display.update()
    return roll_result


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Trigger dice roll animation on space bar press
                result = roll_dice_animation()
                print(f"You rolled a {result}")

    pygame.display.update()

# Quit pygame
pygame.quit()
