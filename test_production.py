import unittest
import production

class TestProduction(unittest.TestCase):

    def test_remove_duplicates(self):
        input = [1,1,2,2]
        output = [1,2]
        self.assertListEqual(output,production.remove_duplicates(input))

    def test_square_numbers(self):
        input = list(range(11))
        output = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertListEqual(output, production.square_numbers(input))


if __name__ == "__main__":
    unittest.main()
