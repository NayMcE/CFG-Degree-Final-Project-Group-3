import pygame
import random
import sys

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

# List of positions with cups (extra roll granted)
CUPS_POSITIONS = [2, 7, 24]

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
    28: 17,  #rabbit_hole
    17: 12,  #rabbit_hole
    12: 1,  #rabbit_hole
    4: 10,  #ladder
    11: 22,  #ladder
    18: 29  #ladder
}


class GamePopup:
    def __init__(self, screen, width, height, background_color, border_color, font):
        self.screen = screen
        self.width = width
        self.height = height
        self.background_color = background_color
        self.border_color = border_color
        self.font = font

    def display_rules(self):
        """Display a pop-up window with the game rules."""
        rules = [
            "Welcome to Alice in Wonderland: Rabbit Holes and Ladders!",
            "",
            "Rules:",
            "1. Press the SPACEBAR to roll the dice.",
            "2. You are Alice and will play first. Then the computer, the Cheshire Cat, will play next. "
            "Players take turns moving based on the dice roll.",
            "3. Ladders move you up; rabbit holes bring you down to the rabbit hole below.",
            "4. First player to reach position 30 wins!",
            "",
            "Press ENTER to start the game.",
        ]

        popup = pygame.Surface((self.width, self.height))
        popup.fill(self.background_color)

        # Draw a border around the pop-up
        pygame.draw.rect(popup, self.border_color, popup.get_rect(), 5)

        # Font settings
        title_font = pygame.font.Font(None, 48)

        # Draw the title
        title = title_font.render("Game Rules", True, (0, 0, 0))
        popup.blit(title, ((self.width - title.get_width()) // 2, 20))

        # Render each line of the rules
        y_offset = 70
        for line in rules:
            split_lines = line.split('\n')
            for sub_line in split_lines:
                text = self.font.render(sub_line, True, (0, 0, 0))
                popup.blit(text, (20, y_offset))
                y_offset += 40

        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(popup, ((WIDTH + SIDE_PANEL_WIDTH - self.width) // 2, (HEIGHT - self.height) // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

    def display_winner(self, winner_name):
        """Display a pop-up announcing the winner."""
        popup = pygame.Surface((self.width, self.height))
        popup.fill(self.background_color)

        # Draw a border around the pop-up
        pygame.draw.rect(popup, self.border_color, popup.get_rect(), 5)

        # Winner text
        text = self.font.render(f"{winner_name} wins!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        popup.blit(text, text_rect)

        # Show the popup
        self.screen.fill((0, 0, 0))
        self.screen.blit(popup, ((WIDTH + SIDE_PANEL_WIDTH - self.width) // 2, (HEIGHT - self.height) // 2))
        pygame.display.update()
        pygame.time.delay(2000)


def roll_dice_animation():
    roll_count = 10  # Number of frames in the roll animation
    for i in range(roll_count):
        # Display random dice face during the animation
        random_face = random.choice(dice_images)
        # Clear the dice animation area
        screen.fill(WHITE, (770, 250, DICE_SIZE, DICE_SIZE))
        screen.blit(random_face, (770, 250))  # Animation position
        # draw_side_panel(3)  # Keep the side panel visible
        pygame.display.update()
        pygame.time.delay(50)  # Short delay to simulate animation

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
        19: (610, 140), 20: (490, 140), 21: (370, 140), 22: (250, 140), 23: (130, 140), 24: (20, 140),
        25: (20, 20), 26: (130, 20), 27: (250, 20), 28: (370, 20), 29: (490, 20), 30: (610, 20)
    }
    return board_positions.get(position, (0, 0))


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

    def move(self, steps):
        self.position += steps
        if self.position > 100:  #maximise the size of the screen
            self.position = 100

        if self.position in ladders_and_rabbit_holes:
            self.position = ladders_and_rabbit_holes[self.position]

        # update the character position
        x, y = get_screen_position(self.position)
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


#create players
Alice = Player(1, player_images[0])
Cat = Player(2, player_images[1])

players_group = pygame.sprite.Group(Alice, Cat)


# Usage in Main Loop
def main():
    popup = GamePopup(screen, 800, 500, WHITE, PINK, font)
    popup.display_rules()

    running = True
    dice_roll = 1
    player_roll = 0
    computer_roll = 0
    current_player = Alice
    player_turn = True

    while running:
        screen.blit(background_image, (0, 0))
        draw_side_panel(player_roll, computer_roll, dice_roll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                dice_roll = roll_dice_animation()
                player_roll = dice_roll
                current_player.move(dice_roll)
                player_turn = False


                if current_player.position in CUPS_POSITIONS:
                    print(f"{current_player.name} landed on a cup! Extra roll granted!")
                    continue

                if current_player.position >= 30:
                    winner_name = 'Alice' if current_player == Alice else 'The Cheshire Cat'
                    popup.display_winner(winner_name)
                    running = False
                    break


                if not player_turn:
                    dice_roll = roll_dice_animation()
                    computer_roll = dice_roll
                    Cat.move(dice_roll)
                    player_turn = True


                if current_player.dice_roll != 6:
                     current_player = Cat if current_player == Alice else Alice

    players_group.draw(screen)
    pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
