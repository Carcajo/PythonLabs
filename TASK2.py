def get_float_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            float_input = float(user_input)
            return float_input
        except ValueError:
            print("Error. Try input digit")


def calculate(num1, num2, operation):
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'sub':
        print(num1 - num2)
    elif operation == 'mult':
        print(num1 * num2)
    elif operation == 'div':
        if num2 == 0:
            print("Error: division by zero")
            return None
        else:
            print(num1 / num2)
    else:
        print("Error: invalid operation")
        return None

calculate(3, 5, "add")
