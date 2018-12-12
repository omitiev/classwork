'''
Необходимо реализовать дескриптор Price который позволяет выставлять атрибут price в пределах от 0 до 100

class Book:
   price = Price()

   def __init__(self, author, title, price):
       self.author = author
       self.title = title
       self.price = price

   def __str__(self):
       return "{0} - {1}".format(self.author, self.title)
'''


class Price:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value in range(101):
            instance.__dict__[self.name] = value
            return instance.__dict__[self.name]
        raise ValueError('Price should be between 0 and 100')

    def __set_name__(self, owner, name):
        self.name = name


class Book:
   price = Price()

   def __init__(self, author, title, price):
       self.author = author
       self.title = title
       self.price = price

   def __str__(self):
       return "{0} - {1}".format(self.author, self.title)


book = Book('oleksii', 'test', 12)
print(book.author)
print(book.title)
print(book.price)
book.price = 99
print(book.price)
book.price = 109

# book_1 = Book("Author", "Title", 50)
# book_2 = Book("Author 2", "Title 2", 60)
# print(book_2.price) # => 60
# print(book_1.price) # => 60