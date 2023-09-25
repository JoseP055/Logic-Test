# Fizz Buzz Test (Write a function that prints numbers from 1 to 100 with a newline between each number... Replacing the following:
# Multiples of 3 with the word "fizz"
# Multiples of 5 with the word "buzz"
# Multiples of both with the word "fizzbuzz")

print("Fizz Buzz Test")


def FizzBuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

FizzBuzz()
