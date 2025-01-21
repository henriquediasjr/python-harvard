import sys

try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)

try: 
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    sys.exit(1)

print(f"{x} / {y} = {result}")