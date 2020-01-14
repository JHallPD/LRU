from collections import OrderedDict


class LRUOD:
    def __init__(self, size):
        if not isinstance(size, int) or int(size) <= 0:
            raise ValueError
        self.max = size
        self.cache = OrderedDict()

    def cache_max(self):
        return self.max

    def get(self, key):
        try:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        except (KeyError, ValueError):
            pass

    def put(self, key, value):
        if key in self.cache:
            self.delete(key)
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)
        if len(self.cache) > self.max:
            self.cache.popitem(last=False)

    def print(self):
        for key, value in self.cache.items():
            print(key, ': ', value)
        return ''

    def reset(self):
        self.cache.clear()

    def delete(self, key):
        try:
            del self.cache[key]
        except (KeyError, ValueError):
            pass


def main():
    print("Creating LRU with size: 4")
    cache = LRUOD(4)
    print("using put 4 time")
    cache.put('1', 'Hall')
    cache.put('2', 'Jeff')
    cache.put('3', 'Canada')
    cache.put('4', 'Ontario')
    print(cache.print())
    print("using get for key 2, Expecting Value: Hall")
    v = cache.get('2')  # expected return value is Hall
    print(v)
    print("using put 2 time")
    cache.put('5', 'GeorgeTown')
    cache.put('6', 'Python')
    print(cache.print())
    print("using get for key 1, Expecting Value: None")
    v = cache.get('1')  # expected return value is None , kicked from cache
    print(v)
    print("using get for key 1, Expecting Value: None")
    cache.delete('1')
    v = cache.get('1')  # expected return value is None , delete no-op
    print(v)
    print("Printing LRUOD cache")
    print(cache.print())
    print("Resetting LRUOD cache then attempting to print")
    cache.reset()
    print(cache.print())


if __name__ == "__main__":
    main()
