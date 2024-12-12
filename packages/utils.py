from functools import wraps

cache = {}
calculated = 0
cached = 0
def memoize(func):
    @wraps(func)
    def decorated(*args):
        global calculated
        global cached
        if args in cache:
            cached+=1
            return cache[args]
        calculated+=1
        result = func(*args)
        cache[args] = result
        return cache[*args]

    return decorated

def getStats():
    return (calculated, cached)