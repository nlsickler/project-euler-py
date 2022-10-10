import unittest

def list_multiples(max_multiple):
    vals = range(1, max_multiple)
    multiples = map(lambda x: x if (x%3 == 0 or x%5 ==0) else None, vals)
    return [mult for mult in multiples if mult is not None]


class TestProj(unittest.TestCase):
    def test10(self):
        vals = list_multiples(10)
        self.assertTrue(3 in vals)
        self.assertTrue(5 in vals)
        self.assertTrue(6 in vals)
        self.assertTrue(9 in vals)
        self.assertFalse(None in vals)
        self.assertEqual(4, len(vals))

    def test2(self):
        vals = list_multiples(2)
        self.assertEqual(0, len(vals))

    # 33 multiples of 3
    # 19 multiples of 5
    # 15, 30, 45, 60, 75, 90 are double counted
    # 33+19-6=46
    def test100(self):
        vals = list_multiples(100)
        self.assertEqual(46, len(vals))

if __name__ == '__main__':
    unittest.main()
