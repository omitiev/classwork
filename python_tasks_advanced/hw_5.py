"""
создать функцию для копирования файлов

```def copy_file(file_name, copy_name=None):
    pass```
`copy_file("log.txt", "log_copy.txt")` создаст копию переданного файла `log.txt` с именем `log_copy.txt`
в случае если имя копии не передано `copy_name=None` - предлагается добавить цифру к имени файла
(по аналогии с операционными системами)
"""

def copy_file(file_name, copy_name=None):
    copy_name = copy_name if copy_name else ''.join(str(file_name.rpartition('.')[0])
                                                    + '(copy).'
                                                    + str(file_name.rpartition('.')[2]))
    file_to_copy = open(file_name, "rt")
    content = file_to_copy.readlines()
    file_to_copy.close()
    new_file = open(copy_name, "at")
    [new_file.write(i) for i in content]
    new_file.close()
    return None


copy_file("log.txt", "log_copy.txt")
copy_file("log.txt")


