# Написать программу, которая переводит в верхний регистр второе слово (слово - последовательность символов между двумя пробелами).
# Например: “abc def ghj” -> “abc DEF ghj”

print("==========================================================")
print("task 9")
print("==========================================================")

str_1 = str(input("Please, enter any text: "))
print("Thanks! Your texts are: \n%s" % str_1)
lst_1 = str.split(str_1)
index = int(len(lst_1))
print("As you can see your text contains %.d words" % index)
word = int(input("Please select the serial number of word which you want to make in UPPER case:"))
if word >= 1 and index >= word:
    print("OK, I\'ll change for you the word #%.d" % word)
    lst_1[word - 1] = lst_1[word - 1].upper()
    print("After some changes your text looks like that:\n", " ".join(lst_1))
else:
    print("Your text doesn\'t have such word")

# Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20". В этой строке указаны имя писателя и через символ * даты рождения и смерти.
# Даты указаны в формате "YYYY-MM-DD". Требуется написать программу, которая по переданной строке определит возраст писателя и вернет его имя и возраст.
# Например, для строки "Leo Tolstoy*1828-08-28*1910-11-20" программа должна вернуть: "Leo Tolstoy", 82. Месяцы и дни можно игнорировать.

print("==========================================================")
print("task 10")
print("==========================================================")

cond = str(input(
    "Please, enter condition for the task in the next way name*birth date*death date (date should be in the next format YYYY-MM-DD): "))
print("You entered next condition : \n%s" % cond)
name1_lst = cond.split('*')
name1_lst[1] = name1_lst[1].split('-')
name1_lst[2] = name1_lst[2].split('-')
age = int(name1_lst[2][0]) - int(name1_lst[1][0])
print()
if age >= 0:
    print("I can make a conclusion that " + name1_lst[0] + " died at %d" % age)
else:
    print("Something wrong in condition")
