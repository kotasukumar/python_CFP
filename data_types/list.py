my_list = [1, 2, 3, 4, 5, 6]

my_list[1] = 10
print(my_list.index(10))

print(my_list)

my_list.append(7)
print(my_list)

my_list.remove(4)
print(my_list)

my_list.remove(my_list[3])
print(my_list)

dublicate = (8, 9, 10)
my_list.insert(7, dublicate)
print(my_list)

my_list.append([1,2,3])
print(my_list)

my_list.append([1,2,3])
print(my_list)


