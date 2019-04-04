import unittest
from StringMethod import count_letter


class TestStringMethod(unittest.TestCase):
    def test_count(self):
        result = count_letter("AAA", "A")
        expected = 3
        self.assertEqual(result, expected)

    def text_count_other_string(self):
        result = count_letter("ABBA", "A")
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
