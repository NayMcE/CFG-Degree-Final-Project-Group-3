#import db connection and functions
from db_utils import save_player_details, save_player_items, save_player_actions, fetch_player_stats, close_connection

# save the players
save_player_details("Alice")
save_player_details("Cheshire Cat")


#store data in database during gameplay
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.tc:
                    save_player_items("Teacup")
                elif event.key == pygame.l:
                    save_player_actions("Climbed ladder")
                elif event.key == pygame.rh:
                    save_player_actions("Fell in rabbit hole")


#display stats at the end of the game
stats = fetch_player_stats()
    print("\nGame Over!:")
    for stat in stats:
        print(
            f"Player: {stat[0]}, Extra rolls: {stat[1]}, "
            f"Ladders Climbed: {stat[2]}, Rabbit Holes Fallen Into: {stat[3]}")

#close connection
finally:
    close_connection()
