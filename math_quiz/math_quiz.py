import random

def function_A(min, max):
    """
    function returns a random integer between min and max
    :return: Random integer.
    """
    return random.randint(min, max)

def function_B():
    """
    function to return either addition, subtraction oder multiplication as char
    :return: one random operator of three
    """
    return random.choice(['+', '-', '*'])

def function_C(number1, number2, operator):
    """
    calculates an operation with two numbers and an operator
    :param number1: number 1 for given operation
    :param number2: number 2 for given operation
    :param operator: gives the operation that should be calculated
    :return: function to be calculated,
    """
    product = f"{number1} {operator} {number2}"
    if operator == '+': addedNumbers = number1 + number2
    elif operator == '-': addedNumbers = number1 - number2
    else: addedNumbers = number1 * number2
    return product, addedNumbers

def math_quiz():
    start = 0
    end = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for iteration in range(end):
        #create two random numbers and an operator
        number1 = function_A(1, 10)
        number2 = function_A(1, 5)
        try:
            operator = function_B()
        except:
            print("An Exception occured!")

        #create the function and the calculated operation
        PROBLEM, ANSWER = function_C(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        #wait for user to answer the created operation
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            start += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {start}/{end}")

if __name__ == "__main__":
    math_quiz()
