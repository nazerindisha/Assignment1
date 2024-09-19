# Function Definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    else:
        return x % y

# Main Program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    # User Input Handling
    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a number between 1 and 5.")
            return
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Conditional Logic and Output Formatting
        if choice == 1:
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == 4:
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result:.2f}")
        elif choice == 5:
            result = modulus(num1, num2)
            if result == "Error! Modulus by zero.":
                print(result)
            else:
                print(f"{num1} % {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator program
calculator()
