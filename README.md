# Python Calculator

## Overview
This Python program provides a simple command-line calculator that can perform basic mathematical operations, including addition, subtraction, multiplication, division, and integer remainder division.

## Features
- Supports basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Integer remainder division (`~`)
- Parses user input for mathematical expressions.
- Computes and displays results dynamically.
- Handles multiple calculations in a session.

## Constants
The following constants represent mathematical operations:
```python
ADDITION = "+"
SUBTRACTION = "-"
MULTIPLICATION = "*"
DIVISION = "/"
INTEGER_REMAINDER_DIVISION = "~"
```

## Functions
### `calculate(text_input: str) -> int | float | tuple`
Parses the input string and performs the corresponding mathematical operation.

### `parse_number(text_input: str, operation: str) -> list`
Splits the input string into two operands based on the operation symbol.

### `addition_numbers(numbers: list) -> int`
Adds two numbers and returns the sum.

### `subtraction_numbers(numbers: list) -> int`
Subtracts two numbers and returns the difference.

### `multiplication_numbers(numbers: list) -> int`
Multiplies two numbers and returns the product.

### `division_numbers(numbers: list) -> float`
Divides two numbers and returns the quotient.

### `division_integer_remainder(numbers: list) -> tuple`
Performs integer division and returns both the quotient and remainder.

### `do_calculation(counter: int)`
Prompts the user for mathematical expressions and calculates results based on the number of iterations specified.

### `main()`
Runs the program, prompting the user for the number of calculations and processing them accordingly.

## Usage
To run the calculator, execute the script in a Python environment:
```sh
python calculator.py
```
The program will ask for the number of calculations and prompt for expressions:
```sh
Welcome to the Python calculator!
How many calculations do you want to do? 2
What do you want to calculate? 10+5
The answer is 15
What do you want to calculate? 20-4
The answer is 16
```
