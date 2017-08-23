import os


class DirectoryChanger:

    def __init__(self, dir):
        self.dir = dir
        self.old_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.dir)
        print("current dir (enter):", os.getcwd())

    def __exit__(self, *exc_info):
        os.chdir(self.old_dir)
        print("current dir (exit):", os.getcwd())



print(os.getcwd())
try:
    with DirectoryChanger("/home/db/Desktop") as cd:
        print(os.getcwd())
        raise ValueError("smth went wrong")
except:
    pass

print(os.getcwd())