#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calculates the factorial of a number                                    *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Define the Factorial class
class Factorial:
    def __init__(self):
        # Constructor that can initialize any necessary properties
        pass

    def calculate_factorial(self, num):
        """Calculates the factorial of a given number."""
        if num == 0:
            return 1
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

    def run(self, min_val, max_val):
        """Calculates factorials for numbers between min_val and max_val inclusive."""
        # Ensure that the min value is less than or equal to the max value
        if min_val > max_val:
            print("Error: min_val should be less than or equal to max_val")
            return
        
        # Print factorials for the range
        for num in range(min_val, max_val + 1):
            print(f"Factorial of {num}! is {self.calculate_factorial(num)}")

    def run_next_10(self, start_val):
        """Calculates the next 10 factorials starting from start_val."""
        # Print factorials for the next 10 numbers starting from start_val
        for num in range(start_val, start_val + 11):
            print(f"Factorial of {num}! is {self.calculate_factorial(num)}")


# Function to handle input and decide which method to call
def handle_input(input_value):
    try:
        if '-' in input_value:
            if input_value.startswith('-'):
                # Handle input like '-hasta' (e.g., -10), range from 1 to that number
                end = int(input_value[1:])
                factorial_calculator = Factorial()
                factorial_calculator.run(1, end)
            elif input_value.endswith('-'):
                # Handle input like 'start-' (e.g., 30-), next 10 factorials from start
                start = int(input_value[:-1])
                factorial_calculator = Factorial()
                factorial_calculator.run_next_10(start)
            else:
                # Handle input like 'start-end' (e.g., 4-8), range from start to end
                start, end = map(int, input_value.split('-'))
                factorial_calculator = Factorial()
                factorial_calculator.run(start, end)
        else:
            # If it's a single number, calculate its factorial
            num = int(input_value)
            factorial_calculator = Factorial()
            print(f"Factorial of {num}! is {factorial_calculator.calculate_factorial(num)}")
    except ValueError:
        # If the input is not valid, show an error
        print("Please enter a valid number or range in the 'start-end' format.")
        sys.exit()

# Check if the user provided an argument from the command line
if len(sys.argv) == 1:
    # If no argument is passed, ask the user to enter a number or a range
    input_value = input("You must provide a number or a range (start-end): ")
    handle_input(input_value)
else:
    # If the user passed an argument, use it directly
    input_value = sys.argv[1]
    handle_input(input_value)
