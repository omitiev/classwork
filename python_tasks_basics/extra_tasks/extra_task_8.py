# A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: “The quick brown fox jumps over the lazy dog”.
# Your task here is to write a function to check a sentence to see if it is a pangram or not.


import default


default.start(8)


def is_pangram(usr_str):
    counter = 0
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    for i in alphabet:
        if i in list(usr_str):
            counter += 1
    return counter == len(alphabet)


str4check = str(input("Please enter your string for checking: "))
print("Your string is pangram? ", is_pangram(str4check))


default.end()

# can be squeezed to:
#
# counter = sum([1 for c in alphabet if c in usr_str])
# and taking into account string module, you can go even further:
#
# return sum([1 for c in alphabet if c in usr_str]) == len(string.ascii_lowercase)
# Also, a user can enter capitals, so this should also be handled correctly:
#
# return sum([1 for c in alphabet if c.lower() in usr_str]) == len(string.ascii_lowercase)
