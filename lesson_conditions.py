a = 10
b = 2
result = a / b
print(result)

# if <condition>: -> True
#     true line 1
#     true line 2
#     true line x
# else:
#     false line 1
#     false line 2
#     false line x

a = 10
b = 0

if b == 0:
    print("Error: division by zero")
else:
    result = a / b
    print(result)


if b != 0:
    result = a / b
    print(result)
else:
    print("Error: division by zero")


a = 10
b = 0

is_zero = b == 0

def is_zero(value):
    return value == 0

if is_zero(b):
    print("Error: division by zero")
else:
    result = a / b
    print(result)