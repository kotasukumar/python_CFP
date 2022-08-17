string = input("Enter any: ")
new_string = ''
print(string)
for char in string:
    if char != ' ':
        new_string += char
print(new_string)
