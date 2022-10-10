import unittest

def find_highest_factor(input):
    return max(get_prime_factors(input))

def get_prime_factors(input):
    factors = [1]
    iter = 2
    while(input != 1):
        if(input%iter == 0):
            if iter not in factors:
                factors.append(iter)
            input = input / iter
            iter = 2
            continue
        iter += 1


    return factors



class TestProj(unittest.TestCase):
    def testFactors(self):
        vals = get_prime_factors(1*2*3*5*7)
        self.assertTrue(2 in vals)
        self.assertTrue(3 in vals)
        self.assertTrue(5 in vals)
        self.assertTrue(7 in vals)
        self.assertTrue(5, len(vals))

    def testPrimeNumber(self):
        vals = get_prime_factors(7793)
        self.assertTrue(7793 in vals)

    def testLargestSimple(self):
        self.assertTrue(7, find_highest_factor(1*2*3*5*7))

    def testLargestFactorPrime(self):
        self.assertTrue(7793, find_highest_factor(7793))

if __name__ == '__main__':
    unittest.main()
