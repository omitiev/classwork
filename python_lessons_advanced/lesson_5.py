# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
# u = User(first_name="Guido", last_name="Van Rossum")
#
#
# print(u.first_name, u.last_name)
# print(u.get_name())

# ###################################################################
#
# class BaseUser:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
# class User(BaseUser):
#     pass
#
# class Admin(BaseUser):
#     def __init__(self, first_name, last_name, position):
#         self.position = position
#         super().__init__(first_name, last_name)
#
#
# u = User(first_name="Guido", last_name="Van Rossum")
# a = Admin("Oleksii", "Mitiev", "admin")
#
# print(u.first_name, u.last_name)
# print(u.get_name())
# print(a.get_name())
# print(a.position)


# ###################################################################
#
# class BaseUser:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
# class User(BaseUser):
#     pass
#
# class Admin(User):
#     _created_users = []
#
#     def __init__(self, first_name, last_name, position):
#         self.position = position
#         super().__init__(first_name, last_name)
#
#     def create_user(self, first_name, last_name):
#         user = User(first_name, last_name)
#         self._created_users.append(user)
#         return user
#
#     def get_created_users(self):
#         return self._created_users
#
#
#
# u = User(first_name="Guido", last_name="Van Rossum")
# a = Admin("Oleksii", "Mitiev", "admin")
#
# names = (("Oleg", "Grogoriev"),("Namtalia", "Bosk"),("Andrew", "Done"),("Jack", "Kirby"))
# for first_name, last_name in names:
#     a.create_user(first_name, last_name)
#
# print(u.first_name, u.last_name)
# print(u.get_name())
# print(a.get_name())
# print(a.position)
#
# u = a.create_user("John", "Doe")
# print(u.get_name())
# print(a.get_created_users())

###################################################################
#
# class BaseUser:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
#
# class User(BaseUser):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.friends = []
#
#     def __repr__(self):
#         return "{}: {} {}".format(self.__class__.__name__, self.first_name, self.last_name)
#
#     def say_hello_to(self, user):
#         return self.friends.append(user)
#
#
# class GenerateOperationsMixin:
#     def get_test_names(self):
#         return ("Oleg", "Grigoriev"), ("Mikael", "Bosk"), ("Andrew", "Done"), ("Jack", "Kirby")
#
#     def generate_test_users(self):
#         for first_name, last_name in self.get_test_names():
#             self.create_user(first_name, last_name)
#
#
# class Admin(GenerateOperationsMixin, User):
#     _created_users = {}
#
#     def __init__(self, first_name, last_name, position):
#         self.position = position
#         super().__init__(first_name, last_name)
#
#     def create_user(self, first_name, last_name):
#         user = User(first_name, last_name)
#         username = first_name + last_name
#         self._created_users[username] = user
#         return user
#
#     def get_user(self, username):
#         return self._created_users.get(username)
#
#     def get_created_users(self):
#         return self._created_users.items()
#
#
# # u = User(first_name="Guido", last_name="Van Rossum")
# admin = Admin("Oleksii", "Mitiev", "admin")
#
#
#
# # print(u.first_name, u.last_name)
# # print(u.get_name())
# # print(admin.get_name())
# # print(admin.position)
# #
# u = admin.create_user("John", "Doe")
# # print(u.get_name())
#
# print(admin.get_created_users())
#
# admin.generate_test_users()
# print(admin.get_user("JohnDoe"))
# print(admin.get_created_users())
# john = admin.get_user("JohnDoe")
# oleg = admin.get_user("OlegGrigoriev")
# print(john, oleg)
#
# john.say_hello_to(oleg)
# print(john.friends)


########################################################

class BaseUser:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class User(BaseUser):
    def __init__(self, *args):
        self.friends = {}
        self.age_check = 10
        super().__init__(*args)


    def check_user(self, user):
        error_msg = "{} age diff is more than {} years"
        if not abs(int(self.age) - int(user.age)) <= self.age_check:
            raise ValueError(error_msg.format(user.get_name(), self.age_check))

    def say_hello_to(self, user):
        self.check_user(user)
        user_name = user.get_name()

        if not self.friends.get(user_name):
            self.friends[user_name] = user
            user.say_hello_to(self)

        # if int(user.age) - 10 <= int(self.age):
        #    return self.friends.append(user)
        # raise ValueError("too old")

    def __repr__(self):
        spec_str = "{}: {} {}, gender:{}, age:{}"
        return spec_str.format(self.__class__.__name__,
                               self.first_name,
                               self.last_name,
                               self.gender,
                               self.age)


class GenerateOperationsMixin:
    def get_test_names(self):
        return (('John', 'Doe', 'male', '20'),
                ('Sansa', 'Stark', 'female', '25'),
                ('Carl', 'Carlson', 'male', '15'),
                ('Thor', 'Odinson', 'male', '30'),
                ('Bruce', 'Wayne', 'male', '35'))

    def generate_test_users(self):
        for params in self.get_test_names():
            self.create_user(*params)


class Admin(GenerateOperationsMixin, User):
    _created_users = {}

    def __init__(self, first_name, last_name, position):
        self.position = position
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self, *args):
        user = User(*args)
        self._created_users[user.get_name()] = user
        return user

    def get_user(self, username):
        return self._created_users.get(username)

    def get_created_users(self):
        return self._created_users.items()


admin = Admin("internal", "user", "admin")
admin.generate_test_users()
# print(admin.get_created_users())
carl = admin.get_user("Carl Carlson")
john = admin.get_user("John Doe")
bruce = admin.get_user("Bruce Wayne")

carl.say_hello_to(john)
carl.say_hello_to(bruce)
john.say_hello_to(carl)
carl.say_hello_to(john)
john.say_hello_to(carl)
print(carl.friends)
print(john.friends)