def generate_fibonacci(num):
    if num <= 1:
        return num
    else:
        return generate_fibonacci(num-1) + generate_fibonacci(num-2)


if __name__ == "__main__":
    number = int(input("Enter no.of stages: "))
    for i in range(number):
        print(generate_fibonacci(i))