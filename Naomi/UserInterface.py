import pygame
import random
import sys

from pygame.examples.cursors import image

# Initialize pygame
pygame.init()

# Constants
WIDTH = 720
HEIGHT = 600
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 100
WHITE = (255, 255, 255)
PINK = (252, 116, 183)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Load board images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# load dice images
dice_images = [pygame.transform.scale(pygame.image.load(f"Images/dice_{i}.jpeg"), (DICE_SIZE, DICE_SIZE))
    for i in range(1, 7)]
dice_rect = dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))

# player images
player_images = [
    pygame.image.load('Characters/Alice.png'),
    pygame.image.load('Characters/ChescherCat.png')
]
player_images = [pygame.transform.scale(img, (100, 100)) for img in player_images]


# Function to draw the side panel with dice
def draw_side_panel(dice_roll):
    pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

ladders_and_rabbit_holes = {
    28: 17, #rabbit_hole
    17: 12, #rabbit_hole
    12: 1,  #rabbit_hole
    4: 10, #ladder
    11: 22, #ladder
    18: 29 #ladder
}

# Function to animate dice roll
def roll_dice_animation():
    roll_count = 10  # Number of frames in the roll animation
    for i in range(roll_count):
        # Display random dice face during the animation
        random_face = random.choice(dice_images)
        # Clear the dice animation area
        screen.fill(WHITE, (770, 250, DICE_SIZE, DICE_SIZE))
        screen.blit(random_face, (770,250)) # Animation position
        # draw_side_panel(3)  # Keep the side panel visible
        pygame.display.update()
        pygame.time.delay(50) # Short delay to simulate animation

    # Final roll result
    roll_result = random.randint(1, 6)
    screen.fill(WHITE, (770, 250, DICE_SIZE, DICE_SIZE))
    screen.blit(dice_images[roll_result - 1], (770, 250))
    draw_side_panel(roll_result)  # Update side panel with final roll
    pygame.display.update()
    return roll_result


# map logical board positions to screen coordinates
def get_screen_position(position):
    board_positions = {
        1: (20, 500), 2: (130, 500), 3: (250, 500), 4: (370, 500), 5: (490, 500), 6: (610, 500),
        7: (610, 380), 8: (490, 380), 9: (370, 380), 10: (250, 380), 11: (130, 380), 12: (20, 380),
        13: (20, 260), 14: (130, 260), 15: (250, 260), 16: (370, 260), 17: (490, 260), 18: (610, 260),
        19: (610, 140), 20: (490, 140), 21: (370, 140), 22: (250, 140), 23: (130, 140), 24: (20,140),
        25: (20, 20), 26: (130, 20), 27: (250, 20), 28: (370, 20), 29: (490, 20), 30: (610, 20)
    }
    return board_positions.get(position, (0,0))

class Player(pygame.sprite.Sprite):
    def __init__(self, id, image):
        super().__init__()
        self.id = id
        self.image = image
        self.rect = self.image.get_rect()
        self.position = 1

        # initialise position on board
        x, y = get_screen_position(self.position)
        self.rect.topleft = (x, y)

    def move(self,steps):
        self.position += steps
        if self.position > 100: #maximise the size of the screen
            self.position = 100

        if self.position in ladders_and_rabbit_holes:
            self.position = ladders_and_rabbit_holes[self.position]

        # update the character position
        x, y = get_screen_position(self.position)
        self.rect.topleft = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

#create players
Alice = Player(1, player_images[0])
Cat = Player(2, player_images[1])

players_group = pygame.sprite.Group(Alice, Cat)


# Main game loop
def main():
    running = True
    dice_roll = 1  # Default dice roll to show on the side panel
    current_player = Alice

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
                    # move the current player
                    current_player.move(dice_roll)
                    #switch players after the move
                    current_player = Cat if current_player == Alice else Alice


        players_group.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
# Run the game
    main()
# Quit pygame
    pygame.quit()
