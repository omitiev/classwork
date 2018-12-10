# Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"

print ("==========================================================")
print ("task 7")
print ("==========================================================")

us_date = str(input("Please, enter a date in american way MM.DD.YYYY"))
print ("In US format the date is", us_date)
lst1=us_date.split(".")
eu_date = str(lst1[1])+'.'+str(lst1[0])+'.'+str(lst1[2])
print ("In EU format the date will be", eu_date)

# Написать программу, которая берет две строки и помещает первую строку в середину второй.
# Результат помещается в середину первой.
# Длину строки можно получить с помощью функции len().

print ("==========================================================")
print ("task 8")
print ("==========================================================")

str1 = str(input("Please, enter any text: "))
str2 = str(input("OK, now enter any other text: "))
print("Thanks! Your texts are: \n1.", str1, "\n2.", str2)
index_str1 = int(round(len(str1))/2)
str1_1 = str1[:index_str1]
str1_2 = str1[index_str1:]
index_str2 = int(round(len(str2))/2)
str2_1 = str2[:index_str2]
str2_2 = str2[index_str2:]
new_str2 = str2_1+str1+str2_2
new_str1 = str1_1 + new_str2 + str1_2
print("But I have improved your texts and now they look like a single text - see below:\n", new_str1)

