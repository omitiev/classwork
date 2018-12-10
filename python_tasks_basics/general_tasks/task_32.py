# В программе phone_book (https://github.com/dbradul/python/blob/master/phone_book.py) реализовать следующие функции:
#   +  find_entry_age_phonebook 		# найти все записи с указанным возрастом
#   +  print_phonebook_by_age		# распечатать все записи отсортированные по возрасту
#   +  delete_entry_name_phonebook	# удалить все записи с указанным именем
#   +  print_avr_age				# распечатать средний возраст всех абонентов
#   +  increase_age				# увеличить возраст всем абонентам на заданное пользователем кол-во лет
#   +  <ваша_функция>				# добавить любую функцию, манипулирующую записями (печать, добавление, удаление) в телефонной книге на ваше усмотрение.
# добавить поддержку еще одного поля (например, скайп, адрес, день рождения) и сделайте по нему поиск и печать.
# Т.е. добавить функцию для поиска и обновить существующую функцию печати.
#
# 	При выполнении обратите внимание на обработку ошибок. Например, если при удалении записи с заданным именем нет, то вывести сообщение “Not found!”.


import default
import pickle



default.start(32)


phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "skype_name": None},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "skype_name": None}
             ]

def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Skype:   %20s |" % entry["skype_name"])
    print ()


def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


def print_phonebook_by_age():
    phone_book.sort(key=lambda contact: contact['age'])
    print_phonebook()


def add_entry_phonebook(surname, name, age, phone_number, skype_name):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["skype_name"] = skype_name
    phone_book.append(entry)


def printError(message):
    print ("ERROR: %s" % message)


def printInfo(message):
    print ("INFO: %s" % message)


def find_entry_name_phonebook(name):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_age_phonebook(age):
    idx = 1
    found = False
    for contact in phone_book:
        if contact['age'] == age:
            print_entry(idx, contact)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_phone_number(phone_number):
    idx = 1
    found = False
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            print_entry(idx, contact)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_skype_name(skype_name):
    idx = 1
    found = False
    for contact in phone_book:
        if contact["skype_name"] == skype_name:
            print_entry(idx, contact)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def delete_entry_name_phonebook(name):
    idx = 1
    found = False
    for contact in phone_book:
        if contact['name'] == name:
            print_entry(idx, contact)
            phone_book.remove(contact)
            idx += 1
            found = True
            print("Corresponding contact was removed from Phone book.")
    if not found:
        printError("Not found!!")


def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


def avr_age_of_all_persons():
    total_age = 0
    for contact in phone_book:
        if 'age' in contact:
            total_age += contact['age']
        else:
            continue
    print("Average age for Phone book is %f" % (total_age/len(phone_book)))


def increase_age(number_of_years):
    for contact in phone_book:
        if 'age' in contact:
            contact["age"] += number_of_years


def add_entry_skype_name(name):
    idx = 1
    found = False
    for contact in phone_book:
        if contact["name"] == name:
            skype = str(input("Please enter new skype name for current user: "))
            contact["skype_name"] = skype
            print_entry(idx, contact)
            found = True
    if not found:
        printError("Not found!!")


def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def main():
    while True:
        user_input = ""
        try:
            print ()
            print ()
            print ()
            print ("~ Welcome to phonebook ~")
            print ("Select one of actions below:")
            print ("     1 - Print phonebook entries")
            print ("     2 - Print phonebook entries (by age)")
            print ("     3 - Add new entry")
            print ("     4 - Find entry by name")
            print ("     5 - Find entry by age")
            print ("     6 - Find entry by phone number")
            print ("     7 - Find entry by skype name")
            print ("     8 - Delete entry by name")
            print ("     9 - The number of entries in the phonebook")
            print ("    10 - Avr. age of all persons")
            print ("    11 - Increase age by num. of years")
            print ("    12 - Add skype name")
            print ("-----------------------------")
            print ("     s - Save to file")
            print ("     l - Load from file")
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                print_phonebook_by_age()
            elif choice == 3:
                surname = str(input("    Enter surname: "))
                name = str(input("    Enter name: "))
                age = int(input("    Enter age: "))
                phone_number = str(input("    Enter a phone number:"))
                skype_name = str(input("    Enter a skype name:"))
                add_entry_phonebook(surname, name, age, phone_number, skype_name)
            elif choice == 4:
                name = str(input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 5:
                age = int(input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 6:
                phone_number = str(input("    Enter phone number: "))
                find_entry_phone_number(phone_number)
            elif choice == 7:
                skype_name = str(input("    Enter skype name: "))
                find_entry_skype_name(skype_name)
            elif choice == 8:
                name = str(input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 9:
                count_all_entries_in_phonebook()
            elif choice == 10:
                avr_age_of_all_persons()
            elif choice == 11:
                number_of_years = int(input("    Enter number of years to add to current ages: "))
                increase_age(number_of_years)
            elif choice == 12:
                name = str(input("    Enter user's name: "))
                add_entry_skype_name(name)
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Enter action within range [0..9]")

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            else:
                printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()




default.end()