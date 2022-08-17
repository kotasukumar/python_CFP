puncutaions = '`~!@#$%^&*()_-+={}][><,.?/*\|"'
new_string = ''
string = input("Enter any any: ")
for i in string:
    if i not in puncutaions:
        new_string = new_string + i
print(new_string)