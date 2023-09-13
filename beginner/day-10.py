# functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name
    into new full name"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("Udit", "Gurani"))


# exercise - calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What the first number?"))
num2 = int(input("What the second number"))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operation[operation_symbol]
answer = calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")