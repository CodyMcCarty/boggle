import unittest
from boggle_board import BoggleBoard

class BoggleBoardTestCase(unittest.TestCase):

    def test_is_array_of_underscores(self):
        """When boggle_board is called it makes an array of '_'"""
        test_array_game = BoggleBoard()
        self.assertEqual(test_array_game.board, ['_'] * 16)

    def test_instance (self):
        """When a new game is created, it is an instance of Boggle Board"""
        test_instance_game = BoggleBoard()
        self.assertIsInstance(test_instance_game, BoggleBoard)


if __name__ == '__main__':
    unittest.main()