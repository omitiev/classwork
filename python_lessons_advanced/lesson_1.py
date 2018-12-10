def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ')
    return text.strip(' ').split()[0]


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    index, count = -1, 0
    for s in text:
        if s == symbol:
            count += 1
            index += 1
            if count == 2:
                return index
        else:
            index +=1
    return None


print(second_index("sims", "s"))
assert second_index("sims", "s") == 3
print(second_index("find the river", "e"))
assert second_index("find the river", "e") == 12
print(second_index("hi", " "))
assert second_index("hi", " ") is None
print(second_index("hi mayor", " "))
assert second_index("hi mayor", " ") is None
print(second_index("hi mr Mayor", " "))
assert second_index("hi mr Mayor", " ") == 5


a = "Hello world"
b = " a word "
c = "don't touch it"
d = "greetings, friends"
e = "... and so on ..."
f = "hi"
g = "Hello.World"

a_1 = first_word(a)
b_1 = first_word(b)
c_1 = first_word(c)
d_1 = first_word(d)
e_1 = first_word(e)
f_1 = first_word(f)
g_1 = first_word(g)

print(a_1)
print(b_1)
print(c_1)
print(d_1)
print(e_1)
print(f_1)
print(g_1)