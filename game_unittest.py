
import pygame
import unittest
from unittest import TestCase
from unittest.mock import patch
from game import Player, get_screen_position, ladders_and_rabbit_holes, cup_positions, roll_dice_animation


class TestPlayer(TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.mock_image = pygame.Surface((100, 100))  # Mock image for player

    def setUp(self):
        self.player = Player(1, self.mock_image)

    @patch('random.randint', return_value=3)
    def test_dice_roll_animation(self, mock_randint):
        result = roll_dice_animation()
        mock_randint.assert_called_once_with(1, 6)
        self.assertEqual(result, 3)

    def test_normal_move(self):
        expected = 5
        self.player.move(4)
        result = self.player.position
        self.assertEqual(expected, result)

    def test_ladder_movement(self):
        self.player.position = 4
        expected = ladders_and_rabbit_holes.get(4, 4)
        self.player.move(0)
        result = self.player.position
        self.assertEqual(expected, result)

    def test_rabbit_hole_movement(self):
        self.player.position = 28
        expected = ladders_and_rabbit_holes.get(28, 28)
        self.player.move(0)
        result = self.player.position
        self.assertEqual(expected, result)

    def test_cup_grants_extra_roll(self):
        self.player.position = 1
        self.player.move(1)

        if self.player.position in cup_positions:
            popup_triggered = True
        else:
            popup_triggered = False

        self.assertIn(self.player.position, cup_positions)
        self.assertTrue(popup_triggered)

    def test_move_beyond_maximum(self):
        self.player.position = 28
        expected = 30
        self.player.move(5)
        result = self.player.position
        self.assertEqual(expected, result)

    def test_screen_position_mapping(self):
        self.player.position = 1
        expected = (20, 500)
        result = get_screen_position(self.player.position)
        self.assertEqual(expected, result)

    def test_invalid_move_type(self):
        with self.assertRaises(TypeError):
            self.player.move("invalid")

if __name__ == '__main__':
    unittest.main()
