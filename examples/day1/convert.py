def decimal(number):
    list = []
    while number != 0:
        list.insert(0, number % 2)
        number = number // 2
    print(f"decimal form of {number} is:", list)


def octal(number):
    list = []
    while number != 0:
        list.insert(0, number % 8)
        number = number // 8
    print(f"Octal form of {number} is:", list)


def hexadecimal(number):
    list = []
    while number != 0:
        list.insert(0, number % 16)
        number = number // 16
    print(f"Hexadecimal form of {number} is:", list)


if __name__ == "__main__":
    number = int(input("Enter any number: "))
    decimal(number)
    octal(number)
    hexadecimal(number)
