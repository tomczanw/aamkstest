import unittest


class TestS2(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_one(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
