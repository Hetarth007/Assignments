def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_operation_choice():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:
        choice = get_operation_choice()
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operation = operations[choice]
        result = operation(num1, num2)
        print(f"The result is: {result}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            break

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()
