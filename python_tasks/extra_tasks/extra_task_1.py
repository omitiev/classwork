import default


default.start(1)


def reverse_str(string):
    return string[::-1]

s_1 = input("Please enter the string for reverse:")
s_2 = reverse_str(s_1)
print("Have a look at new string: %s" % s_2)

default.end()
