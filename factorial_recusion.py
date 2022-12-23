def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Please enter the number to calcualte factorial:"))
print("The factorial of {0} is: {1}".format(x,factorial(x)))
