
num = int(input("What number? "))

def factorial (number):
    print (number)
    if number == 1:
        return 1
    return factorial(number - 1) * number

print (f"Factorial of {num} is", factorial(num))


