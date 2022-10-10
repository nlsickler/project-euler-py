import functools
import unittest

def get_prime_factors(input):
    factors = [1]
    iter = 2
    while(input != 1):
        if(input%iter == 0):
            factors.append(iter)
            input = input / iter
            iter = 2
            continue
        iter += 1

    return factors

def smallest_mult(input_num):
    inputs = range(input_num, 1, -1)
    factors = []

    for x in inputs:
        primes = get_prime_factors(x)

        for p in primes:
            to_add = primes.count(p) - factors.count(p)
            if to_add > 0:
                for i in range(to_add):
                    factors.append(p)

    return functools.reduce(lambda a,b: a*b, factors)




class TestProj(unittest.TestCase):
    def test(self):
        res = smallest_mult(10)
        self.assertEqual(2520, res)

    def test20(self):
        res = smallest_mult(20)
        self.assertEqual(232792560, res)

if __name__ == '__main__':
    unittest.main()
