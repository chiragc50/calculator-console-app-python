def menu():
    print("-------------Calculator-------------")
    print("1.[A]dd")
    print("2.[M]ulitply")
    print("3.[S]ubstract")
    print("4.[D]ivide")
    print("5.Press Any Key to Exit")


def get_two_numbers():
    try:
        number1 = int(input("Enter number one:"))
        number2 = int(input("Enter number two:"))
        return number1, number2
    except ValueError:
        print("❌ Please enter valid numbers")
        return None, None


def add():
    number1, number2 = get_two_numbers()
    if number1 is None or number2 is None:
        return None
    return number1 + number2


def multiply():
    number1, number2 = get_two_numbers()
    if number1 is None or number2 is None:
        return None
    return number1 * number2


def subtract():
    number1, number2 = get_two_numbers()
    if number1 is None or number2 is None:
        return None
    return number1 - number2


def divide():
    number1, number2 = get_two_numbers()
    if number1 is None or number2 is None:
        return None
    if number2 == 0:
        print("❌ Can't divide by zero")
        return
    return number1 / number2


operations = {
    "a": ("Addition", add),
    "m": ("Multiplication", multiply),
    "s": ("Subtract", subtract),
    "d": ("Divide", divide),
}

menu()
while True:
    user_input = input("Enter: ").lower()

    if user_input not in operations:
        break

    title, fun = operations[user_input]

    print("\n--------------------Addition--------------------")
    result = fun()
    if result is not None:
        print(result)
    menu()

print("-------------Thank You-------------")
