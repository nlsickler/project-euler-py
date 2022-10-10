import unittest

def calc_sum(max_val):
    vals = create_fib([1, 2], max_val)
    return sum([val for val in vals if val % 2 == 0])


def create_fib(fib_list, max_val):
    new_val = sum(fib_list[-2:])
    if(new_val > max_val):
        return fib_list

    fib_list.append(new_val)
    return create_fib(fib_list, max_val)


class TestProj(unittest.TestCase):

    def testBase(self):
        self.assertEqual(2, calc_sum(2))

    def test4(self):
        self.assertEqual(2, calc_sum(4))

    def test9(self):
        self.assertEqual(10, calc_sum(9))


    def test4mil(self):
        self.assertEqual(4_613_732, calc_sum(4_000_000))

if __name__ == '__main__':
    unittest.main()
