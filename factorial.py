def factorial(a):
    if a <= 1:
        return a
    return a * factorial(a-1)

for i in range(1,50):
    print("Factorial of {} is {}".format(i,str(factorial(i))))
