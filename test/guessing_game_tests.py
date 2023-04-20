import unittest
from guessing_game_for_test import check_guess


class GuessingGameTests(unittest.TestCase):
    def test_guess_is_answer(self):
        result = check_guess(2, 2)
        self.assertTrue(result)

    def test_guess_is_not_answer(self):
        result = check_guess(5, 1)
        self.assertFalse(result)

    def test_guess_is_outside_range(self):
        result = check_guess(233, 1)
        self.assertFalse(result)

    def test_guess_is_wrong_type(self):
        result = check_guess(2, '2')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
