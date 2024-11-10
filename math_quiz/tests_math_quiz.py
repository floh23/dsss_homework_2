import unittest
from math_quiz.math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if a valid operator was created
        for _ in range(1000):
            operator = function_B()
            self.assertTrue((operator == '+' or operator == '-' or operator == '*'))


    def test_function_C(self):
            #Test if the created test cases are calculated correctly
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 4, '-', '5 - 4', 1),
                (2, 6, '*', '2 * 6', 12),
                (4, 6, '+', '4 + 6', 10),
                (10, 1, '-', '10 - 1', 9),
                (4, 4, '*', '4 * 4', 16)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                actualOutput = function_C(num1, num2, operator)
                self.assertTrue(actualOutput == (expected_problem, expected_answer))

if __name__ == "__main__":
    unittest.main()
