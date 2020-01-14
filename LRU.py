class LRU:
    def __init__(self, size):
        if not isinstance(size, int) or int(size) <= 0:
            raise ValueError
        self.max = size
        self.keys = []
        self.cache = {}

    def cache_max(self):
        return self.max

    def get(self, key):
        try:
            self.put(key, self.cache[key])
            return self.cache.get(key)
        except (KeyError, ValueError):
            pass

    def put(self, key, value):
        if key in self.cache:
            self.delete(key)
        self.keys.append(key)
        for _ in range(len(self.keys) - self.max):
            self.delete(self.keys.pop(0))
        self.cache[key] = value

    def print(self):
        for key, value in self.cache.items():
            print(key, " : ", value)
        return ''

    def reset(self):
        self.cache.clear()
        self.keys.clear()

    def delete(self, key):
        try:
            del self.cache[key]
            self.keys.pop(self.keys.index(key))
        except (KeyError, ValueError):
            pass


def main():
    print("Creating LRU with size: 4")
    cache = LRU(4)
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
    v = cache.get('1') # expected return value is None , delete no-op
    print(v)
    print("Printing LRU cache")
    print(cache.print())
    print("Resetting LRU cache then attempting to print")
    cache.reset()
    print(cache.print())


if __name__ == "__main__":
    main()
