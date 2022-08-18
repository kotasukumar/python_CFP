def check_palindrome(param):
    if param == param[::-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


if __name__ == "__main__":
    print(check_palindrome(str(input("Enter a word to check palindrome: "))))