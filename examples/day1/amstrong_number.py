def dividing_number(number_to_separate):
    check = 0
    for i in number_to_separate:
        check = check + int(i) ** len(number_to_separate)
    return check


if __name__ == "__main__":
    number = input("Enter a number: ")
    cal = dividing_number(input("Enter a number: "))
    if cal == int(number):
        print("Entered number is an Armstrong number")
    else:
        print("Entered number is not Armstrong number")
