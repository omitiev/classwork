class MySupress:
    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.exception_type)  # bets way (compare the 1 elem with the 2)

        # 1 bad variant
        # if self.exception_type == exc_type:
        #     return True

        # 2
        # if isinstance(exc_type(), self.exception_type):
        #     return True
        # ==
        # return isinstance(exc_type(), self.exception_type)

with MySupress(KeyError):
    {}['key']

with MySupress(IndexError):
    [][1]

with MySupress(Exception):
    {}['key']


# class Opened:
#     def __init__(self, file_name, mode):
#         self.handler = open(file_name, mode)
#
#     def __enter__(self):
#         return self.handler
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.handler.close()
#         del self.handler

class Opened:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        if not self.file_name or self.mode:
            raise ValueError("name: {} or mode: {} shouldn't be empty".format(
                self.file_name,
                self.mode
            ))

    def __enter__(self):
        self.handler = open(self.file_name, self.mode)
        return self.handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handler.close()



with Opened("file_name.txt", mode="a") as o_file:
    o_file.write("hello")
#
# with Opened("", mode="a") as o_file:
#     o_file.write("hello")
