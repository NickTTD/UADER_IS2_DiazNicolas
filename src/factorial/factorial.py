#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Check if the user provided a command-line argument
if len(sys.argv) == 1:
    # No command-line argument, ask for input
    try:
        num = int(input("Ingrese un número: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        sys.exit()
else:
    # Use the argument as the number
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Por favor ingrese un número válido.")
        sys.exit()

print(f"Factorial {num}! es {factorial(num)}")
