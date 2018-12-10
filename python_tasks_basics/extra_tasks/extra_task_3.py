# Convert a given var name from python_style into CamelizedStyle
# solution(“this_is_var_name”)  -> “ThisIsVarName”

import default


default.start(3)


def new_style(string):
    return ''.join(((string.replace('_',' ')).title()).split())

base_string = str(input("Please enter your string in base format (e.g. this_is_var_name): "))
print("The new string is: ", new_style(base_string))


default.end()
