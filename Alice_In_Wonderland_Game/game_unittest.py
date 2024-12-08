
import pygame
import unittest
from unittest import TestCase
from unittest.mock import patch
from game import Player, get_screen_position, ladders_and_rabbit_holes, cup_positions, roll_dice_animation

class TestPlayer(TestCase):

    def setUp(self):
        pygame.init()
        self.Alice = Player(1, pygame.Surface((100, 100)))
        self.Cat = Player(2, pygame.Surface((100, 100)))

    @patch('random.randint', return_value=3)
    def test_dice_roll_animation(self, mock_randint):
        """Test that dice roll animation returns the expected value."""
        result = roll_dice_animation()
        mock_randint.assert_called_once_with(1, 6)
        self.assertEqual(result, 3)

    def test_normal_move(self):
        """Test normal movement of players."""
        self.Alice.position = 1
        self.Cat.position = 2

        self.Alice.move(4)
        self.Cat.move(3)

        self.assertEqual(self.Alice.position, 5)
        self.assertEqual(self.Cat.position, 5)

    def test_ladder_movement(self):
        """Test ladder behavior when a player lands on a ladder."""
        self.Alice.position = 4
        self.Alice.move(0)  # Landing on the ladder position

        self.assertEqual(self.Alice.position, ladders_and_rabbit_holes[4])

    def test_rabbit_hole_movement(self):
        """Test rabbit hole behavior when a player lands on a rabbit hole."""
        self.Cat.position = 28
        self.Cat.move(0)  # Landing on the rabbit hole position

        self.assertEqual(self.Cat.position, ladders_and_rabbit_holes[28])

    def test_cup_grants_extra_roll(self):
        self.Alice.position = 1
        self.Alice.move(1)

        if self.Alice.position in cup_positions:
            popup_triggered = True
        else:
            popup_triggered = False

        self.assertIn(self.Alice.position, cup_positions)
        self.assertTrue(popup_triggered)

    def test_move_beyond_maximum(self):
        """Test that a player cannot move beyond the maximum board position."""
        self.Alice.position = 28
        self.Alice.move(5)  # Attempt to move beyond position 30

        self.assertEqual(self.Alice.position, 30)

    def test_screen_position_mapping(self):
        """Test that a player's position maps correctly to screen coordinates."""
        self.Alice.position = 1
        expected = (20, 500)
        result = get_screen_position(self.Alice.position)

        self.assertEqual(result, expected)

    def test_invalid_move_type(self):
        """Test that invalid move inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            self.Alice.move("invalid")  # Pressing anything that's not the spacebar

    def test_two_players_same_position(self):
        """Test that two players can occupy the same position."""
        self.Alice.position = 4
        self.Cat.position = 4

        self.assertEqual(self.Alice.position, self.Cat.position)

    def test_two_players_independent_movement(self):
        """Test that two players move independently."""
        self.Alice.position = 1
        self.Cat.position = 1

        self.Alice.move(9)
        self.Cat.move(4)

        self.assertEqual(self.Alice.position, 10)
        self.assertEqual(self.Cat.position, 5)

    def test_special_position_interaction(self):
        """Test ladder and rabbit hole interactions for multiple players."""
        self.Cat.position = 3
        self.Alice.position = 27

        self.Cat.move(1)  # Triggers ladder
        self.Alice.move(1)  # Triggers rabbit hole

        self.assertEqual(self.Cat.position, ladders_and_rabbit_holes[4])
        self.assertEqual(self.Alice.position, ladders_and_rabbit_holes[28])

    def test_cup_position_interaction(self):
        """Test cup interactions for multiple players."""
        self.Alice.position = 7
        self.Cat.position = 1

        self.Alice.move(0)  # Lands on cup position
        self.Cat.move(2)  # Moves past cup position

        self.assertIn(self.Alice.position, cup_positions)
        self.assertNotIn(self.Cat.position, cup_positions)


if __name__ == '__main__':
    unittest.main()
