from functools import reduce

numbers = [1, 5, 6, 7, 9, 10, 12, 45]
result = reduce(lambda a, b: a + b, numbers)

print("The sum of the list items is:", result)
