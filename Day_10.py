# Function with Outputs

# first_name = str(input("what is your first name? \n"))
# last_name = str(input("what is your last name?\n"))


def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = (f_name + " " + l_name).title()
    return full_name


# print(format_name(first_name, last_name))


# Calculator Project

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    first_number = float(input("What is your first number? "))
    for symbol in operation:
        print(symbol)
    operator = input("Pick an operation: ")

    calculation_continue = False
    while not calculation_continue:
        second_number = float(input("What is your second number? "))
        result = operation[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {result}")

        next_turn = input(f"do you want to calculate another number with {result}? type: Yes or No")
        if next_turn == "No":
            calculation_continue = True
            calculator()
        else:
            first_number = result


calculator()
