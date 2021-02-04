import unittest
import calculator as c

class TestCalculator(unittest.TestCase):

    def test_addition(self): #Addition
        self.assertEqual(c.addition(1, 2), 3)
        self.assertEqual(c.addition(7, 2), 9)

    def test_subtraction(self): #Division test
        self.assertEqual(c.subtraction(1, 2), -1)
        self.assertEqual(c.subtraction(6, 4), 2)

    def test_multiplication(self): #Multiplication test
        self.assertEqual(c.multiplication(4, 2), 8)
        self.assertEqual(c.multiplication(1, 2), 2)

    def test_division(self): #Division test
        #Divide by zero handled in readInput()
        self.assertEqual(c.division(4, 2), 2)
        self.assertEqual(c.division(1, 2), 0.5)

    def test_input(self): #ReadInput() test
        #Correct inputs
        self.assertTrue(c.readInput("1 + 1"))
        self.assertTrue(c.readInput("1 - 1"))
        self.assertTrue(c.readInput("1 * 1"))
        self.assertTrue(c.readInput("1 / 1"))

        #Incorrect inputs
        self.assertFalse(c.readInput(""))
        self.assertFalse(c.readInput("1.2 + 32.3"))
        self.assertFalse(c.readInput("1/2"))
        self.assertFalse(c.readInput("213 / 1231 2"))
        self.assertFalse(c.readInput("1 + 1 + 1"))
        self.assertFalse(c.readInput("2 _ 3"))
        self.assertFalse(c.readInput("a + b"))

        #Divide by Zero handling
        self.assertFalse(c.readInput("3 / 0"))

if __name__ == "__main__":
    unittest.main()
