from typing import Tuple

ADDITION = "+"
SUBTRACTION = "-"
MULTIPLICATION = "*"
DIVISION = "/"
INTEGER_REMAINDER_DIVISION = "~"

"""
Mathematical Operation Constants

This module defines constants representing various mathematical operations. 
These constants can be used in expressions or functions to identify the 
operation being performed.

Constants:
    ADDITION (str): Represents the addition operation ("+").
    SUBTRACTION (str): Represents the subtraction operation ("-").
    MULTIPLICATION (str): Represents the multiplication operation ("*").
    DIVISION (str): Represents the division operation ("/").
    INTEGER_REMAINDER_DIVISION (str): Represents the integer remainder division operation 
"""


def calculate(text_input: str):
    """
    Parses a mathematical expression from a string and performs the appropriate operation.

    This function identifies whether the input string contains an addition, subtraction,
    multiplication, or division operation. Based on the operation present, it extracts the
    first and second numbers from the string and performs the corresponding arithmetic
    operation (addition, subtraction, multiplication, or division).

    The operations are represented by global constants (e.g., ADDITION, SUBTRACTION, MULTIPLICATION,
    DIVISION).

    Parameters:
        text_input (str): A string containing a mathematical expression with two operands
                          and an operation symbol. For example, "45+32" or "100/5".

    Returns:
        int or float: The result of the arithmetic operation between the two numbers.
                      Addition, subtraction, and multiplication will return an integer.
                      Division may return a float if the result is not a whole number.

    Example:
        calculate("45+32")
        77
        calculate("100-20")
        80
        calculate("6*7")
        42
        calculate("100/4")
        25.0
    """
    return_value = 0.0

    if ADDITION in text_input:
        return_value =  addition_numbers(parse_number(text_input,ADDITION))
    elif SUBTRACTION in text_input:
        return_value =  subtraction_numbers(parse_number(text_input,SUBTRACTION))
    elif MULTIPLICATION in text_input:
        return_value =  multiplication_numbers(parse_number(text_input,MULTIPLICATION))
    elif INTEGER_REMAINDER_DIVISION in text_input:
        return_value =  division_integer_remainder(parse_number(text_input,INTEGER_REMAINDER_DIVISION))
    else:
        return_value = division_numbers(parse_number(text_input,DIVISION))

    return return_value

def parse_number(text_input: str,operation: str)-> list:
    """
    Splits the input string into two parts based on the specified operation.

    This function takes a string containing a mathematical expression and splits it
    into a list of two elements, separating the input at the specified operation symbol.

    Args:
        text_input (str): The input string containing a mathematical expression,
                          such as '45+32' or '100-20'.
        operation (str): The operation symbol used to split the input string,
                         such as '+', '-', '*', or '/'.

    Returns:
        list: A list of two substrings representing the operands in the mathematical expression.

    Example:
        parse_number('45+32', '+')
        ['45', '32']
        parse_number('100-20', '-')
        ['100', '20']
    """

    return text_input.split(operation)

def addition_numbers(numbers: list)-> int:
    """
    Adds two integers and returns their sum.

    This function takes two integer list arguments, adds them together, and returns the result.

    Parameters:
        numbers (list): The Augend and Addend to be added.

    Returns:
        int: The sum of `Augend` and `Addend`.

    Example:
        addition_numbers(['3', '5'])
        8
    """
    first_number, second_number = numbers

    return int(first_number) + int(second_number)

def subtraction_numbers(numbers: list)-> int:
    """
    Subtracts two integers and returns their Difference.

    This function takes two list integer arguments, subtracts them together, and returns the difference.

    Parameters:
        numbers (list): The Minuend and Subtrahend

    Returns:
        int: The difference of `Minuend` and `Subtrahend`.

    Example:
        subtraction_numbers(['4', '1'])
        3
    """

    first_number, second_number = numbers

    return int(first_number) - int(second_number)

def multiplication_numbers(numbers: list)-> int:
    """
    Multiply two integers and returns their Product.

    This function takes two list integer arguments, multiply them together, and returns the product.

    Parameters:
        numbers (list): The Multiplicand and Multiplier

    Returns:
        int: The Product of `Multiplicand` and `Multiplier`.

    Example:
        multiplication_numbers(['2','2')
        4
    """

    first_number, second_number = numbers

    return int(first_number) * int(second_number)

def division_numbers(numbers: list)-> float:
    """
    Divide two integers and returns their Quotient.

    This function takes two list integer arguments, divide them together, and returns the quotient.

    Parameters:
        numbers (list): The Dividend and Divisor

    Returns:
        int: The Quotient of `Dividend` and `Divisor`.

    Example:
        division_numbers(['4','2'])
        2
    """

    first_number, second_number = numbers

    return int(first_number) / int(second_number)

def division_integer_remainder(numbers: list) -> tuple[int, int]:
    """
     Divides two integers and returns the integer quotient and remainder.

     This function performs integer division on `first_number` by `second_number`
     and calculates the remainder. It returns both the quotient and the remainder
     as a list.

     Parameters:
         numbers (list): The numerator, the number to be divided an The denominator, the number by which `first_number` is divided.

     Returns:
         list: A list containing two elements:
               - The integer quotient of the division (first_number // second_number).
               - The remainder of the division (first_number % second_number).

     Example:
         division_integer_remainder(['10','3'])
         [3, 1]
         division_integer_remainder(['20','4'])
         [5, 0]
     """

    first_number, second_number = numbers

    integer_result = int(first_number) // int(second_number)
    remainder_result = int(first_number) % int(second_number)

    return integer_result,remainder_result

def do_calculation(counter: int):
    """
    Prompts the user to input mathematical expressions and calculates the results.

    This function runs a loop for a specified number of iterations (determined by `counter`).
    In each iteration, it asks the user for a mathematical expression, calculates the result
    using the `calculate` function, and prints the answer.

    Parameters:
        counter (int): The number of times the user will be prompted to enter a calculation.

    Example:
        do_calculation(3)
        What do you want to calculate? 10+5
        The answer is 15
        What do you want to calculate? 20-4
        The answer is 16
        What do you want to calculate? 6*7
        The answer is 42
    """

    for counter in range(counter):
        user_input = input("What do you want to calculate? ")

        result = calculate(user_input)

        if INTEGER_REMAINDER_DIVISION in user_input:
            integer_division, remainder_division = calculate(user_input)
            print(f"The answer is {integer_division}")
            print(f"The remainder is {remainder_division}")
        else:
            print(f"The answer is {result}")

print("Welcome to the Python calculator!")
do_calculation(int(input("How many calculations do you want to do? ")))

