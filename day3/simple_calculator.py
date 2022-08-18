def addition(fi_value, sec_value):
    return fi_value + sec_value


def subtraction(f_value, sec_value):
    return f_value - sec_value


def multiplication(f_value, sec_value):
    return f_value * sec_value


def division(f_value, sec_value):
    return f_value / sec_value


if __name__ == "__main__":
    user_input = 1
    while user_input != 5:
        print("1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exit ")
        user_input = int(input("choice the operation you want to do: "))
        if user_input != 5:
            first_value = int(input("Enter first value: "))
            second_value = int(input("Enter second value: "))
            if user_input == 1:
                print(f"Addition of {first_value} and {second_value} is", addition(first_value, second_value))
            if user_input == 2:
                print(f"Subtraction of {first_value} and {second_value} is", subtraction(first_value, second_value))
            if user_input == 3:
                print(f"Multiplication of {first_value} and {second_value} is", multiplication(first_value, second_value))
            if user_input == 4:
                print(f"Division of {first_value} and {second_value} is", division(first_value, second_value))
            if user_input == 5:
                break
