start_number = int(input('Enter the starting number: '))
end_number = int(input('Enter the ending number: '))

for i in range(start_number,end_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} Fizz')
    elif i % 5 == 0:
        print(f'{i} Buzz')
    else:
        print(i)