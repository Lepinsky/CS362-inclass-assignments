import unittest
import fibonacci as f

# Pytest Method
def test_fibonacci():
    # Special Cases
    assert f.fibonacci(0) == 0
    assert f.fibonacci(1) == 1

    # Normal Cases
    assert f.fibonacci(2) == 1
    assert f.fibonacci(6) == 8
    assert f.fibonacci(9) == 34

'''
# Unittest Method
class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self): # Assuming inputs are valid whole numbers
        # Special Cases
        self.assertEqual(f.fibonacci(0), 0)
        self.assertEqual(f.fibonacci(1), 1)
        self.assertEqual(f.fibonacci(2), 1)

        # Normal Cases
        self.assertEqual(f.fibonacci(6), 8)
        self.assertEqual(f.fibonacci(9), 34)

if __name__ == "__main__":
    unittest.main()
'''
