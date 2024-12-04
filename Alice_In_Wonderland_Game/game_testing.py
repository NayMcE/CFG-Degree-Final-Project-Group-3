import unittest
from unittest.mock import patch
from game import Player, ladders_and_rabbit_holes, get_screen_position
import pygame
#
# class TestRollDiceAnimationRandomness(unittest.TestCase):
#
#     @patch('random.choice')
#     @patch('random.randint')
#     def test_random_functionality(self, mock_randint, mock_choice):
#         # Mock dice images
#         dice_images = ["face1", "face2", "face3", "face4", "face5", "face6"]
#         mock_choice.side_effect = dice_images  # Simulate random choices
#         mock_randint.return_value = 4  # Simulate the final roll result
#
#         # # Mock global variables
#         global dice_images
#         dice_images = dice_images
#
#         # Run the function
#         result = roll_dice_animation()
#
#         # Verify random.choice was called 10 times (for the animation frames)
#         self.assertEqual(mock_choice.call_count, 10)
#
#         # Verify random.randint was called once to determine the final result
#         mock_randint.assert_called_once_with(1, 6)
#
#         # Check that the function returns the mocked final roll result
#         self.assertEqual(result, 4)

class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize pygame to avoid errors when loading assets
        pygame.init()
        # Mock an image for player creation
        cls.mock_image = pygame.Surface((100, 100))

    def setUp(self):
        # Create a Player instance for testing
        self.player = Player(1, self.mock_image)

    def test_move_normal(self):
        """Test normal movement (no ladder or rabbit hole)."""
        self.player.move(3)  # Move 3 steps from position 1
        self.assertEqual(self.player.position, 4)

    def test_move_with_ladder(self):
        """Test movement where a ladder is present."""
        self.player.position = 4  # Set initial position to 4
        self.player.move(0)  # No steps, just test ladder logic
        self.assertEqual(self.player.position, 10)  # Ladder from 4 to 10

    def test_move_with_rabbit_hole(self):
        """Test movement where a rabbit hole is present."""
        self.player.position = 28  # Set initial position to 28
        self.player.move(0)  # No steps, just test rabbit hole logic
        self.assertEqual(self.player.position, 17)  # Rabbit hole from 28 to 17

    def test_move_beyond_max(self):
        """Test movement beyond the maximum position (100)."""
        self.player.position = 98  # Set near end of board
        self.player.move(5)  # Try to move 5 steps
        self.assertEqual(self.player.position, 100)  # Should be capped at 100

    def test_get_screen_position(self):
        """Test that screen coordinates match board position."""
        self.player.position = 1
        x, y = get_screen_position(self.player.position)
        self.assertEqual((x, y), (0, 480))  # Expected screen position for tile 1


if __name__ == '__main__':
    unittest.main()
