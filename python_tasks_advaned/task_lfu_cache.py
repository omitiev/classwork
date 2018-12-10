import functools


def new_lfu_cache(func, maxsize=64):
   cache = {}
   info = {'hits': 0, 'misses': 0, 'maxsize': maxsize, 'cache_len': len(cache)}
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
       wrapper.last_args = args, kwargs
       wrapper.cache = cache
       wrapper.info = info
       if str(wrapper.last_args) in cache:
           cache[str(wrapper.last_args)][0] += 1
           info['hits'] += 1
           return cache[str(wrapper.last_args)][1]
       else:
           if len(cache) < maxsize:
               cache[str(wrapper.last_args)] = [1, func(*args, **kwargs)]
               info['misses'] += 1
               info['cache_len'] = len(cache)
               return cache[str(wrapper.last_args)][1]
           else:
               cache[str(wrapper.last_args)] = cache.pop(min(cache.items(), key=lambda t: t[1]))
               cache[str(wrapper.last_args)] = [1, func(*args, **kwargs)]
               info['misses'] += 1
               info['cache_len'] = len(cache)
               return cache[str(wrapper.last_args)][1]

   def last_call():
       return "last call info: args {}".format(wrapper.last_args)

   def new_cache_info():
       return "cache info: {}".format(wrapper.info)

   def new_cache_clear():
       cache.clear()
       wrapper.info = {'hits': 0, 'misses': 0, 'maxsize': maxsize, 'cache_len': len(cache)}
       return None


   wrapper.last_args = "not called"
   wrapper.info = "not called"
   wrapper.new_cache_info = new_cache_info
   wrapper.last_call = last_call
   wrapper.new_cache_clear = new_cache_clear

   return wrapper

@new_lfu_cache
def test_func(*args):
   return args

# не поддерживатся ключевые аргументы при кешировании (edited)

print(test_func.new_cache_info())
print(test_func(*range(10)))
print(test_func.new_cache_info())
print(test_func.last_call())
print(test_func.last_args)
print(test_func(*range(5)))
print(test_func.last_call())
print(test_func.last_args)
print(test_func.new_cache_info())
print(test_func(*range(8)))
print(test_func.last_call())
print(test_func.last_args)
print(test_func(*range(10)))
print(test_func.last_call())
print(test_func.last_args)
print(test_func(*range(10)))
print(test_func.last_call())
print(test_func.last_args)
print(test_func.new_cache_info())
test_func.new_cache_clear()
print(test_func.new_cache_info())