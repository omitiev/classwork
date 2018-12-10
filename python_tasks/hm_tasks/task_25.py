import default


default.start(25)

def factorial_rec(n):
    if n == 0:
        return 1
    else:
        n = n * factorial_rec(n - 1)
        return n

a = int(input("Please enter a number: "))
print("The factorial of number %d is %d" % (a, factorial_rec(a)))

default.end()
