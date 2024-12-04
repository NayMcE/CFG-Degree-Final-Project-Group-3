import pygame
import random
import sys

# from pygame.examples.cursors import image


# Initialize pygame
pygame.init()

# Constants
WIDTH = 720
HEIGHT = 600
SIDE_PANEL_WIDTH = 200
DICE_SIZE = 100
WHITE = (255, 255, 255)
PINK = (252, 116, 183)
font = pygame.font.SysFont('Montserrat', 24)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Rabbit Holes and Ladders")

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
    pygame.image.load('Characters/CheshireCat.png')
]
player_images = [pygame.transform.scale(img, (100, 100)) for img in player_images]


# Function to draw the side panel with dice
def draw_side_panel(player_roll, computer_roll, dice_roll):
    pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
    screen.blit(dice_images[dice_roll - 1], dice_rect.topleft)  # Draw dice based on roll

    # display rolls on sie panel for each character after they have rolled
    text = font.render(f"Alice rolled: {player_roll}", True, (0, 0, 0))
    screen.blit(text, (WIDTH + 10, 100))
    text = font.render(f"Cat rolled: {computer_roll}", True, (0, 0, 0))
    screen.blit(text, (WIDTH + 10, 150))

ladders_and_rabbit_holes = {
    28: 17, #rabbit_hole
    17: 12, #rabbit_hole
    12: 1,  #rabbit_hole
    4: 10, #ladder
    11: 22, #ladder
    18: 29 #ladder
}


def display_rules():
    """Display a pop-up window with the game rules."""
    rules = [
        "Welcome to Alice in Wonderland: Rabbit Holes and Ladders!",
        "",
        "Rules:",
        "1. Press the SPACEBAR to roll the dice.",
        "2. You are Alice and you will play first. Then the computer, the Cheshire\nCat will play next. Players take turns moving based on the dice roll.",
        "3. Ladders move you up; rabbit holes bring you down to the rabbit\nhole below.",
        "4. First player to reach position 30 wins!",
        "",
        "Press ENTER to start the game.",
    ]

    # Create a surface for the rules pop-up
    popup_width = 800
    popup_height = 500
    popup = pygame.Surface((popup_width, popup_height))
    popup.fill(WHITE)

    # Draw a border around the pop-up
    pygame.draw.rect(popup, PINK, popup.get_rect(), 5)

    # Font settings
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 48)

    # Draw the title
    title = title_font.render("Game Rules", True, (0, 0, 0))
    popup.blit(title, ((popup_width - title.get_width()) // 2, 20))

    # Render each line of the rules
    y_offset = 70
    for line in rules:
        # split lines containing \n into seperate lines
        split_lines = line.split('\n')
        for sub_line in split_lines:
            text = font.render(sub_line, True, (0, 0, 0))
            popup.blit(text, (20, y_offset))
            y_offset += 40

    # Blit the pop-up onto the screen and wait for the user to press ENTER
    while True:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(popup, ((WIDTH + SIDE_PANEL_WIDTH - popup_width) // 2, (HEIGHT - popup_height) // 2))
        pygame.display.update()

        # Wait for the user to press ENTER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Exit the rules screen


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
    # draw_side_panel(roll_result)  # Update side panel with final roll
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

def display_winner(winner_name):
    font = pygame.font.Font(None, 74)
    text = font.render(f"{winner_name} wins!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)  # Show the text on the screen
    pygame.display.update()  # Update the display
    pygame.time.delay(2000)  # Delay for 2 seconds to show the message
    popup_width = 800
    popup_height = 500
    popup = pygame.Surface((popup_width, popup_height))
    popup.fill(WHITE)
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(popup, ((WIDTH + SIDE_PANEL_WIDTH - popup_width) // 2, (HEIGHT - popup_height) // 2))
    pygame.display.update()

    # Draw a border around the pop-up
    pygame.draw.rect(popup, PINK, popup.get_rect(), 5)

# Main game loop
def main():
    display_rules()
    running = True
    dice_roll = 1  # Default dice roll to show on the side panel
    player_roll = 0 # store Alice's roll
    computer_roll = 0 # store the Cat's roll
    current_player = Alice
    player_turn = True

    while running:
        # Draw the board and side panel
        screen.blit(background_image, (0, 0))
        draw_side_panel(player_roll, computer_roll, dice_roll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE:
                    # Trigger dice roll animation on space bar press
                    dice_roll = roll_dice_animation()
                    player_roll = dice_roll #save Alice's roll
                    # move the current player
                    current_player.move(dice_roll)
                    #switch players after the move
                    player_turn = False

                # Check for a win
            if current_player.position >= 30:
                winner_name = 'Alice' if current_player == Alice else 'The Cheshire Cat'
                display_winner(winner_name)  # Display the winner on the screen
                running = False
                break

            # if it's the computer's turn (Cheshire Cat), roll automatically
            if not player_turn:
                dice_roll = roll_dice_animation()
                computer_roll = dice_roll  # save Cat roll
                Cat.move(dice_roll)
                player_turn = True

        # Draw players and update the screen
        players_group.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
# Run the game
    main()
# Quit pygame
    pygame.quit()
