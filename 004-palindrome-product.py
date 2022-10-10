import unittest

def find_max(input_range):
    max_val = [0,0,0]
    for res in find_all_in_input_range(input_range):
        if res[2] > max_val[2]:
            max_val = res

    return max_val

def find_all_in_input_range(input_range):
    vals = []
    for x in input_range:
        for y in input_range:
            res = get_palindrome_product(x, y)
            if(res is not None):
                vals.append(res)

    return vals


def get_palindrome_product(x, y):
    res = x*y
    if str(res) == str(res)[::-1]:
        return [x, y, res]
    else:
        return None

class TestProj(unittest.TestCase):
    def testBaseProductFunc(self):
        self.assertEqual([11,11,121], get_palindrome_product(11, 11))

    def testFind(self):
        result = find_max(range(1,100))
        self.assertEqual(9009, result[2])

    def testRunProject(self):
        res = find_max(range(100,1000))
        print(res)
        self.assertNotEqual(0, res)



if __name__ == '__main__':
    unittest.main()
