from art import logo

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
    "/": divide
}


def calculation():
    print(logo)
    accumulate = True
    n1 = (float(input("What's the first number?")))

    while accumulate:
        operator = input("Choose an operator: +, -, *, /")
        n2 = float(input("What's the next number?"))
        result = operations[operator](n1,n2)

        print(f"{n1} {operator} {n2} = {result}")
        accumulate_result = input(f"Type y to continue calculating with {result}, or tyope n to start a new calculation")

        if accumulate_result == "y":
            n1 = result
        else:
            accumulate = False
            calculation()

calculation()





