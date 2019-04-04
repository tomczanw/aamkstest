import unittest
from NumberMethod import sumTwoNumber


class TestNumberMethod(unittest.TestCase):
    def test_sum(self):
        result = sumTwoNumber(2, 4)
        expected = 6
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
