"""
calc.py
Emily Jacobson
9/9/2024
"""
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def continue_calc(orig_result):
    for operator in operations:
        print(operator)
    operation = input("Pick an operation: ")
    n2 = float(input("What is the next number? "))
    result = operations[operation](orig_result, n2)
    print(f"{orig_result} + {n2} = {result}")
    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ").lower()
    if cont == "y":
        continue_calc(result)
    elif cont == "n":
        print("\033c", end="")
        print(art.logo)
        new_clac()

def new_clac():
    n1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)
    operation = input("Pick an operation: ")
    n2 = float(input("What is the next number? "))
    result = operations[operation](n1, n2)
    print(f"{n1} + {n2} = {result}")
    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ").lower()
    if cont == "y":
        continue_calc(result)
    elif cont == "n":
        print("\033c", end="")
        print(art.logo)
        new_clac()

print(art.logo)
new_clac()