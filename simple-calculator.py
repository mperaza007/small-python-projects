def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed!"
    return x/y


def main():
    print("\n====Simple Calculator===")
    print("Select operation:"
          "\n1. Addition (+)"
          "\n2. Subtraction (-)"
          "\n3. Multiplication (X)"
          "\n4.Division (/)")

    while True:
        choice = input("\nEnter choice(1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a number between 1 and 4.")
        else:
            break
    try:
        num1 = float(input("Ener first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter a valid number!")
    if choice == "1":
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")

    again = input("Do you want to perform another calculation? (y/n): ")
    if not again.startswith('y'):
        print("Goodbye!")
        return
    else:
        main()


main()
