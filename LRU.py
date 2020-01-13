class LRU:
    def __init__(self, size):
        self.max = size
        self.keys = []  # used a list because lists have order
        self.cache = {}  # used a dict because it prevents duplicated keys

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
    cache = LRU(4)
    cache.put('1', 'Hall')
    cache.put('2', 'Jeff')
    cache.put('3', 'Canada')
    cache.put('4', 'Ontario')
    v = cache.get('2')  # expected return value is Hall
    print(v)
    cache.put('5', 'GeorgeTown')
    cache.put('6', 'Python')
    v = cache.get('1')  # expected return value is None , kicked from cache
    print(v)
    cache.delete('1')
    v = cache.get('1') # expected return value is None , delete no-op
    print(v)
    print(cache.print())
    cache.reset()
    print(cache.print())


if __name__ == "__main__":
    main()
