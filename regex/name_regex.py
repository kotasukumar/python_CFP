import re

# name validation
name = "Sukumar"
pattern = '([A-Z]{1})([a-z]{2,})'
result = re.match(pattern, name)

if result:
    print("valid name")
else:
    print("invalid name")


# validation for mobile number
number = "7563614401"
pattern1 = '([0-9]{10})'
response = re.match(pattern1, number)

if response:
    print("valid number")
else:
    print("Invalid number")
