def binary(number):
    binary = ""
    while number > 0:
        if number % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        number = number // 2
    return binary

number = int(input("Enter a number to convert to binary: "))
print(f'Binary representation: {binary(number)}')