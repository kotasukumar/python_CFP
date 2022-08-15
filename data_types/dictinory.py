my_dictinory = {'a': [[5], [1]], 'b': [6]}

temp = []
for i in my_dictinory.keys():
    temp.append(my_dictinory[i])
print(temp)

print(my_dictinory)

my_dictinory['a'] = [1, 2]
my_dictinory['b'] = [1, 5]
print(my_dictinory)

temp = my_dictinory.get('a')
print(temp)
temp.remove(2)

my_dictinory['b'] = [[4], [1]]
print(my_dictinory)

print(my_dictinory)

for i in my_dictinory.values():
    print(i)
