#!/usr/bin/python3
# Python program to display all the prime numbers within an interval


# Define the lower and upper bounds of the interval
lower = 1
upper = 500

# Print the range for which we are finding prime numbers
print("Prime numbers between", lower, "and", upper, "are:")

# Iterate through each number in the range from lower to upper (inclusive)
for num in range(lower, upper + 1):
    # Prime numbers are greater than 1, so we start checking from 2
    if num > 1:
        # Check for factors of num starting from 2 up to num-1
        for i in range(2, num): 
            # If num is divisible by i, it is not a prime number
            if (num % i) == 0:
                # If we find a divisor, break the loop
                break
        else:
            # If no divisors are found, num is a prime number and we print it
            print(num)
