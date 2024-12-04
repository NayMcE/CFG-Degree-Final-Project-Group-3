import pygame
import random
import sys

# List of positions with cups (extra roll granted)
CUPS_POSITIONS = [2, 7, 24]

def display_winner(winner_name):
    font = pygame.font.Font(None, 74)
    text = font.render(f"{winner_name} wins!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)  # Show the text on the screen
    pygame.display.update()  # Update the display
    pygame.time.delay(2000)  # Delay for 2 seconds to show the message

def main():
    display_rules()
    running = True
    current_player = Alice

    while running:
        # Draw the board and side panel
        screen.blit(background_image, (0, 0))
        draw_side_panel(current_player.roll, Cat.roll, current_player.dice_roll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Roll the dice for the current player
                current_player.dice_roll = roll_dice_animation()
                current_player.move(current_player.dice_roll)

                # Check if the player landed on a cup position
                if current_player.position in CUPS_POSITIONS:
                    print(f"{current_player.name} landed on a cup! Extra roll granted!")
                    continue  # Grant another turn without switching players

                # Check for a win
                if current_player.position >= 30:
                    winner_name = 'Alice' if current_player == Alice else 'The Cheshire Cat'
                    display_winner(winner_name)  # Display the winner on the screen
                    running = False
                    break

                # Switch players or grant an extra turn
                if current_player.dice_roll != 6:
                    current_player = Cat if current_player == Alice else Alice

        # Draw players and update the screen
        players_group.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()



