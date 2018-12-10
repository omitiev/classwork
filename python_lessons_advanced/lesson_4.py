import time
from datetime import datetime
import functools
import string

# def logger(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func (*args, **kwargs)
#         end = time.time()
#         return "result = {result}, worktime = {worktime}".format(result = result, worktime = end - start)
#     return wrapper
#
#
# @logger
# def test(*args):
#     time.sleep(1)
#     return args
#
#
# print(test('test'))

###################################################################
#
# def logger(filename):
#     def deco(func):
#         log_format = "{timestamp} function_name = {func_name} result = {result} worktime = {worktime} \n"
#
#         functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func (*args, **kwargs)
#             end = time.time()
#             file = open(filename, "a")
#             file.write(log_format.format(timestamp = datetime.now(), func_name = func.__name__,
#                                          result = result, worktime = end - start))
#
#             file.close()
#             return result
#         return wrapper
#     return deco
#
#
# @logger('log.txt')
# def test(*args):
#     time.sleep(1)
#     return args
#
# for i in range(10):
#     print(test(i))


###################################################################

# def logger(filename):
#     def deco(func):
#         log_format = "{timestamp} function_name = {func_name} result = {result} worktime = {worktime} \n"
#         file_mode = "a"
#
#         functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func (*args, **kwargs)
#             end = time.time()
#             file = open(filename, file_mode)
#             file.write(log_format.format(timestamp = datetime.now(), func_name = func.__name__,
#                                          result = result, worktime = end - start))
#
#             file.close()
#             return result
#         return wrapper
#     return deco

#
# @logger('log.txt')
# def test(*args):
#     time.sleep(1)
#     return args
#
# print(test('z'))

# def new_lfu_cache(func, maxsize=64):
#    cache = {}
#    info = {'hits': 0, 'misses': 0, 'maxsize': maxsize, 'cache_len': len(cache)}
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        wrapper.last_args = args, kwargs
#        wrapper.cache = cache
#        wrapper.info = info
#        if str(wrapper.last_args) in cache:
#            cache[str(wrapper.last_args)][0] += 1
#            info['hits'] += 1
#            return cache[str(wrapper.last_args)][1]
#        else:
#            if len(cache) < maxsize:
#                cache[str(wrapper.last_args)] = [1, func(*args, **kwargs)]
#                info['misses'] += 1
#                info['cache_len'] = len(cache)
#                return cache[str(wrapper.last_args)][1]
#            else:
#                cache[str(wrapper.last_args)] = cache.pop(min(cache.items(), key=lambda t: t[1]))
#                cache[str(wrapper.last_args)] = [1, func(*args, **kwargs)]
#                info['misses'] += 1
#                info['cache_len'] = len(cache)
#                return cache[str(wrapper.last_args)][1]
#
#    def last_call():
#        return "last call info: args {}".format(wrapper.last_args)
#
#    @logger('log.txt')
#    def new_cache_info():
#        return "cache info: {}".format(wrapper.info)
#
#    def new_cache_clear():
#        cache.clear()
#        wrapper.info = {'hits': 0, 'misses': 0, 'maxsize': maxsize, 'cache_len': len(cache)}
#        return None
#
#
#    wrapper.last_args = "not called"
#    wrapper.info = "not called"
#    wrapper.new_cache_info = new_cache_info
#    wrapper.last_call = last_call
#    wrapper.new_cache_clear = new_cache_clear
#
#    return wrapper
#
# @new_lfu_cache
# def test_func(*args):
#    return args
#
# print(test_func.new_cache_info())
# print(test_func(*range(10)))
# print(test_func.new_cache_info())
# print(test_func.last_call())
# print(test_func.last_args)
# print(test_func(*range(5)))
# print(test_func.last_call())
# print(test_func.last_args)
# print(test_func.new_cache_info())
# print(test_func(*range(8)))
# print(test_func.last_call())
# print(test_func.last_args)
# print(test_func(*range(10)))
# print(test_func.last_call())
# print(test_func.last_args)
# print(test_func(*range(10)))
# print(test_func.last_call())
# print(test_func.last_args)
# print(test_func.new_cache_info())
# test_func.new_cache_clear()
# print(test_func.new_cache_info())


###################################################################

def logger(filename):
    def deco(func):
        log_format = "{timestamp} function_name = {func_name} result = {result} worktime = {worktime} \n"
        file_mode = "a"

        functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func (*args, **kwargs)
            end = time.time()
            file = open(filename, file_mode)
            file.write(log_format.format(timestamp = datetime.now(), func_name = func.__name__,
                                         result = result, worktime = end - start))

            file.close()
            return result
        return wrapper
    return deco
#
#
# @logger('log.txt')
# def test(*args):
#     time.sleep(1)
#     return args
#
# print(test('z'))
#
#
#
#
# def is_ascii(test):
#     return all(i in string.ascii_letters + string.punctuation + string.digits for i in test)
#
# def is_ascii(test):
#     return all(ord(i)<= 256 for i in test)
#
# def is_ascii(test):
#     return test.isascii()
#
# print(is_ascii('test'))
# print(is_ascii('тест'))
# print(is_ascii('!'))
# print(is_ascii('1'))


@logger("query_params_log.txt")
def get_query_params(url):
    if url.isascii():
        params = url.partition('/?')[2].split('&')
        return dict([i.split('=') for i in params])
    else:
        print("Not {!r}".format("ascii"))
        return None


print(get_query_params("blabla.com/?a=1&b=2&c=3&d=4"))
print(get_query_params("blaівраbla.com/?a=1&b=2&c=3&d=4"))