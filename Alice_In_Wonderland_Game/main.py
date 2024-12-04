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
font = pygame.font.SysFont('Arial', 24)

# Initialize screen
screen = pygame.display.set_mode((WIDTH + SIDE_PANEL_WIDTH, HEIGHT))
pygame.display.set_caption("Rabbit Holes and Ladders")

# Load board images
background_image = pygame.image.load("Alice-In-Wonderland_Board_Game.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Player images
player_images = [
    pygame.image.load('Characters/Alice.png'),
    pygame.image.load('Characters/CheshireCat.png')
]
player_images = [pygame.transform.scale(img, (100, 100)) for img in player_images]


class Dice:
    def __init__(self):
        self.dice_images = [
            pygame.transform.scale(pygame.image.load(f"Images/dice_{i}.jpeg"), (DICE_SIZE, DICE_SIZE))
            for i in range(1, 7)
        ]
        self.rect = self.dice_images[0].get_rect(center=(WIDTH + SIDE_PANEL_WIDTH // 2, HEIGHT // 2))

    def roll(self):
        """Simulate rolling the dice."""
        roll_result = random.randint(1, 6)
        return roll_result

    def animate_roll(self):
        """Animate the dice roll with random faces."""
        roll_count = 10  # Number of frames in the roll animation
        for _ in range(roll_count):
            random_face = random.choice(self.dice_images)
            screen.fill(WHITE, (770, 250, DICE_SIZE, DICE_SIZE))
            screen.blit(random_face, (770, 250))  # Animation position
            pygame.display.update()
            pygame.time.delay(50)  # Short delay to simulate animation

        # Final roll result
        return self.roll()

class Board:
    def __init__(self):
        self.ladders_and_rabbit_holes = {
            28: 17,  # rabbit hole
            17: 12,  # rabbit hole
            12: 1,   # rabbit hole
            4: 10,   # ladder
            11: 22,  # ladder
            18: 29   # ladder
        }

    def get_screen_position(self, position):
        """Get screen position of a board cell."""
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
        x, y = self.get_screen_position(self.position)
        self.rect.topleft = (x, y)

    def move(self, steps):
        """Move the player by a number of steps, handle ladders/rabbit holes."""
        self.position += steps
        if self.position > 30:  # Max position on board
            self.position = 30
        if self.position in ladders_and_rabbit_holes:
            self.position = ladders_and_rabbit_holes[self.position]

        x, y = self.get_screen_position(self.position)
        self.rect.topleft = (x, y)

    def get_screen_position(self, position):
        """Map logical board positions to screen coordinates."""
        board_positions = {
            1: (20, 500), 2: (130, 500), 3: (250, 500), 4: (370, 500), 5: (490, 500), 6: (610, 500),
            7: (610, 380), 8: (490, 380), 9: (370, 380), 10: (250, 380), 11: (130, 380), 12: (20, 380),
            13: (20, 260), 14: (130, 260), 15: (250, 260), 16: (370, 260), 17: (490, 260), 18: (610, 260),
            19: (610, 140), 20: (490, 140), 21: (370, 140), 22: (250, 140), 23: (130, 140), 24: (20, 140),
            25: (20, 20), 26: (130, 20), 27: (250, 20), 28: (370, 20), 29: (490, 20), 30: (610, 20)
        }
        return board_positions.get(position, (0, 0))

    def draw(self, screen):
        """Draw the player on the screen."""
        screen.blit(self.image, self.rect.topleft)


class UI:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 24)

    def draw_side_panel(self, player_roll, computer_roll):
        pygame.draw.rect(screen, PINK, pygame.Rect(WIDTH, 0, SIDE_PANEL_WIDTH, HEIGHT))  # Side panel background
        # Display rolls on side panel for each character after they have rolled
        text = self.font.render(f"Alice rolled: {player_roll}", True, (0, 0, 0))
        screen.blit(text, (WIDTH + 10, 150))
        text = self.font.render(f"Cat rolled: {computer_roll}", True, (0, 0, 0))
        screen.blit(text, (WIDTH + 10, 150))

    def display_rules(self):
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
            # split lines containing \n into separate lines
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

class Game:
    def __init__(self):
        self.dice = Dice()
        self.board = Board()
        self.ui = UI()
        self.Alice = Player(1, player_images[0])
        self.Cat = Player(2, player_images[1])
        self.players_group = pygame.sprite.Group(self.Alice, self.Cat)
        self.running = True
        self.player_roll = 0
        self.computer_roll = 0
        self.current_player = self.Alice
        self.player_turn = True

    def main_loop(self):
        self.ui.display_rules()  # Display rules screen before starting
        while self.running:
            screen.blit(background_image, (0, 0))
            self.ui.draw_side_panel(self.player_roll, self.computer_roll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.player_turn:
                            self.player_roll = self.dice.animate_roll()
                            self.Alice.move(self.player_roll)
                            self.player_turn = False
                        else:
                            self.computer_roll = self.dice.animate_roll()
                            self.Cat.move(self.computer_roll)
                            self.player_turn = True

            # Draw players
            self.players_group.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.main_loop()
