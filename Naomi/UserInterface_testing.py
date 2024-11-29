import unittest
from unittest.mock import patch
from UserInterface import roll_dice_animation
import random

class TestRollDiceAnimationRandomness(unittest.TestCase):

    @patch('random.choice')
    @patch('random.randint')
    def test_random_functionality(self, mock_randint, mock_choice):
        # Mock dice images
        dice_images = ["face1", "face2", "face3", "face4", "face5", "face6"]
        mock_choice.side_effect = dice_images  # Simulate random choices
        mock_randint.return_value = 4  # Simulate the final roll result

        # # Mock global variables
        global dice_images
        dice_images = dice_images

        # Run the function
        result = roll_dice_animation()

        # Verify random.choice was called 10 times (for the animation frames)
        self.assertEqual(mock_choice.call_count, 10)

        # Verify random.randint was called once to determine the final result
        mock_randint.assert_called_once_with(1, 6)

        # Check that the function returns the mocked final roll result
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
