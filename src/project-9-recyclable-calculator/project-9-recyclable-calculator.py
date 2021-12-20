import art


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operator = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculation():
    print(art.logo)
    continue_calculation = True
    num_1 = float(input("What is the first number: "))

    while continue_calculation:
        operation_symbol = input("Please pick an operator: ")
        num2 = float(input("What is the next number: "))
        print(f"{num_1} {operation_symbol} {num2} = {operator[operation_symbol](num_1, num2)}")
        num_1 = operator[operation_symbol](num_1, num2)
        flag = input(f"Type 'y' to continue calculating with {num_1}, type 'n' to start a new calculation.").lower()
        if flag == 'n':
            continue_calculation = False
            calculation()


calculation()  # Recursion
