vowels = ('a', 'e', 'i', 'o', 'u')
string = input("Enter any sentence: ")
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in {string} is: ", count)
