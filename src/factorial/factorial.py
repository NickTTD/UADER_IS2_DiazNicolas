#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* Calculates the factorial of a number                                    *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Function to calculate the factorial of a number
def factorial(num): 
    # If the number is negative, factorial does not exist
    if num < 0: 
        print("Factorial of a negative number does not exist")
        return 0
    # The factorial of 0 is 1
    elif num == 0: 
        return 1
    else: 
        # Calculate the factorial of positive numbers
        fact = 1
        while(num > 1): 
            fact *= num  # Multiply the current number by the accumulated result
            num -= 1      # Decrease the number
        return fact 

# Function to calculate and display the factorials of numbers in a range
def calculate_factorials_in_range(start, end):
    # Check that the start number is not greater than the end number
    if start > end:
        print("The start number must be less than or equal to the end number.")
        return
    
    # Calculate the factorial for each number in the range
    for num in range(start, end + 1):
        print(f"Factorial of {num}! is {factorial(num)}")

# Check if the user provided an argument from the command line
if len(sys.argv) == 1:
    # If no argument is passed, ask the user to enter a number or a range
    input_value = input("You must provide a number or a range (start-end): ")
    try:
        # If the input contains a dash '-', treat it as a range
        if '-' in input_value:
            if input_value.startswith('-'):
                # Handle case where input is '-hasta' (e.g., -10), range from 1 to that number
                end = int(input_value[1:])
                calculate_factorials_in_range(1, end)  # Call function with start=1, end as specified
            elif input_value.endswith('-'):
                # Handle case where input is 'start-' (e.g., 3-), range from start to 60
                start = int(input_value[:-1])  # Remove the dash and get the start number
                calculate_factorials_in_range(start, 60)  # Call function with start as specified, end=60
            else:
                # Handle regular range (start-end)
                start, end = map(int, input_value.split('-'))  # Split the range and convert to integers
                calculate_factorials_in_range(start, end)  # Call function to calculate factorials
        else:
            # If it's a single number, calculate its factorial
            num = int(input_value)
            print(f"Factorial of {num}! is {factorial(num)}")
    except ValueError:
        # If the input is not valid, show an error
        print("Please enter a valid number or range in the 'start-end' format.")
        sys.exit()
else:
    # If the user passed an argument, use it directly
    try:
        input_value = sys.argv[1]
        # If the argument contains a dash '-', treat it as a range
        if '-' in input_value:
            if input_value.startswith('-'):
                # Handle case where input is '-hasta' (e.g., -10), range from 1 to that number
                end = int(input_value[1:])
                calculate_factorials_in_range(1, end)  # Call function with start=1, end as specified
            elif input_value.endswith('-'):
                # Handle case where input is 'start-' (e.g., 3-), range from start to 60
                start = int(input_value[:-1])  # Remove the dash and get the start number
                calculate_factorials_in_range(start, 60)  # Call function with start as specified, end=60
            else:
                # Handle regular range (start-end)
                start, end = map(int, input_value.split('-'))  # Split the range and convert to integers
                calculate_factorials_in_range(start, end)  # Call function to calculate factorials
        else:
            # If it's a single number, calculate its factorial
            num = int(input_value)
            print(f"Factorial of {num}! is {factorial(num)}")
    except ValueError:
        # If the argument is not valid, show an error
        print("Please enter a valid number or range in the 'start-end' format.")
        sys.exit()
