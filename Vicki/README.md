**ALICE IN WONDERLAND BOARD GAME**

Table of Contents
1. [Overview]
2. [Features]
3. [File structure]
4. [Setup & Installation]
5. [How to play]
6. [Future Enhancements]

--------------------------------------------------
**Overview**

Welcome to the Alice in Wonderland Board Game project! This interactive board game brings Lewis Carroll's enchanting world to life with engaging gameplay and whimsical design elements. Players take on the role of Alice, navigating a board inspired by Snakes and Ladders, complete with themed features such as rabbit holes, ladders, and collectible tea cups.

---------------------------------------------------
**Features**

- **Interactive Gameplay**: Navigate the board as Alice while the Cheshire Cat acts as an automated opponent.
- **Special Mechanics**: Rabbit holes and ladders alter movement, and tea cups grant bonus rolls when collected.
- **Automated Turns**: Dice rolls and movements are managed programmatically.
- **Dynamic Feedback**: A sidebar provides real-time updates on dice rolls, progress, and game events.
- **Themed Design**: Graphics and mechanics are inspired by the Alice in Wonderland universe.
- **Database Integration**: Tracks tea cup collections, game time, and top scores for persistent gameplay data.


----------------------------------------------------------

**File Structure**

The project is organized into the following directories and files:

Alice in Wonderland Game/
├── Characters/
│   ├── Alice.png
│   └── CheshireCat.png
├── Images/
│   ├── BG.jpg
│   ├── TeaCup.png
│   ├── dice_1.jpeg
│   ├── dice_2.jpeg
│   ├── dice_3.jpeg
│   ├── dice_4.jpeg
│   ├── dice_5.jpeg
│   ├── dice_6.jpeg
│   └── rabbit-hole.jpeg
├── database/
│   ├── config.py
│   ├── db_game_code.py
│   ├── db_utils.py
│   ├── requirements.txt.py
│   ├── storage_database.sql
│   └── storage_database_testing.py
├── Alice-In-Wonderland_Board_Game.png
├── game.py
├── game_testing.py
├── requirements.txt
└── README.md

----------------------------------------------------------

**Setup and Installation**

Prerequisites
- **Python 3.7+**
- **MySQL** installed and configured
- Python packages listed in `requirements.txt`

Setup
1. Clone the repository or download the ZIP file and extract it.
2. Install the dependencies from requirements.txt
3. Setup mysql DB - Execute the SQL script to create and initialise the database
4. Configure the database connection:
    Create a config.py file in the root directory with your database credentials:
        USER = "your_username"
        PASSWORD = "your_password"
        HOST = "localhost"
        DATABASE = "storage_database"
5. Run the game

----------------------------------------------------------
**How to Play**

1. Launch the game to see the main menu.
2. Choose "Play" to start the game, "Directions" to view instructions, or "Quit" to exit.
3. Press the spacebar to roll the dice and move Alice across the board.
4. Collect tea cups, avoid rabbit holes, and climb ladders to reach the final square before the Cheshire Cat.
5. The game alternates turns between Alice and the Cheshire Cat, with progress displayed in the sidebar.

----------------------------------------------------------

**Future Enhancements**

- **Multiplayer Support**: Enable multiple players to participate.
- **Custom Themes**: Allow players to select different visual themes.
- **Expanded Mechanics**: Introduce new special squares and collectibles.


----------------------------------------------------------

Enjoy the game, and may the best player win! 🌟