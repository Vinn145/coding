import math

def advanced_calculator():
    print("Welcome to the Advanced Calculator!")
    print("You can perform operations like +, -, *, /, ** (exponentiation), and sqrt (square root).")
    print("Type 'exit' to quit.")
    
    while True:
        expression = input("Enter your expression: ")
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            # Replace sqrt with math.sqrt for square root calculations
            expression = expression.replace('sqrt', 'math.sqrt')
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")