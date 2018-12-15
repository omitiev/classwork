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
        # if isinstance(self.exception_type(), exc_type):
        #     return True

with MySupress(KeyError):
    {}['key']