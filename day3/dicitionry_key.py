my_dect = {1: 2, 3: 4, 5: 6, 7: 8}
key = int(input("Enter a key for search: "))
if key in my_dect.keys():
    print("present")
else:
    print("Not present")
