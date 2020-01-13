from unittest import TestCase
from LRU import LRU


# Run tests in the LRU folder
# Folder: \LRU>
# Command: python -m unittest
class TestLRU(TestCase):
    __test__ = False

    # setup data for the unit tests.
    @classmethod
    def setUpClass(cls):
        max_cache = 4
        cls.lru = LRU(max_cache)
        cls.lruFull = LRU(max_cache)
        cls.lruFull.put('1', 'Test Get 1')
        cls.lruFull.put('2', 'Test Get 2')
        cls.lruFull.put('3', 'Test Get 3')
        cls.lruFull.put('4', 'Test Get 4')


class Tests(TestLRU):

    def test__max(self):
        self.assertEqual(self.lru.cache_max(), 4)

    def test__put(self):
        self.lru.put('1', 'Test Put 1')
        self.lru.put('2', 'Test Put 2')
        self.lru.put('3', 'Test Put 3')
        self.lru.put('4', 'Test Put 4')
        self.assertEqual(self.lru.get("3"), 'Test Put 3')
        self.lru.put('5', 'Test Put 5')
        self.assertEqual(self.lru.get("1"), None)
        self.assertEqual(list(self.lru.cache), self.lru.keys)

    def test__get(self):
        check = self.lruFull.get("2")
        self.assertEqual(check, 'Test Get 2')
        self.lruFull.put('5', 'Test Get 5')
        self.assertEqual(self.lruFull.get("1"), None)
        self.lruFull.put('1', 'Test Get 1')
        self.lruFull.put('2', 'Test Get 2')
        self.lruFull.put('3', 'Test Get 3')
        self.lruFull.put('4', 'Test Get 4')
        self.assertEqual(list(self.lruFull.cache), self.lruFull.keys)

    def test__delete(self):
        self.lruFull.delete('1')
        self.assertEqual(self.lruFull.get("1"), None)
        self.assertNotIn('1', list(self.lruFull.cache))
        self.assertNotIn('1', self.lruFull.keys)

    def test__reset(self):
        self.lruFull.reset()
        self.assertNotIn('1', list(self.lruFull.cache))
        self.assertNotIn('1', self.lruFull.keys)
        self.assertEqual(len(self.lruFull.cache), 0)
        self.assertEqual(len(self.lruFull.keys), 0)
        self.assertEqual(self.lruFull.max, 4)

