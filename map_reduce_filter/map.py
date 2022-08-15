# calculating area of rectangles
length = [14, 25, 67, 18, 69]
width = [4, 6, 2, 55, 56, 66, 5]

area = list(map(lambda l, w: l*w, length, width))

print("Area of Rectangle")
print(area)