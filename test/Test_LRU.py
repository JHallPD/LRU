from unittest import TestCase
from LRU import LRU
from LRUOD import LRUOD


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
        cls.lruod = LRUOD(max_cache)
        cls.lruodFull = LRUOD(max_cache)
        cls.lruodFull.put('1', 'Test Get 1')
        cls.lruodFull.put('2', 'Test Get 2')
        cls.lruodFull.put('3', 'Test Get 3')
        cls.lruodFull.put('4', 'Test Get 4')


# Tests class
# tests cache size, get, put, delete, reset
class Tests(TestLRU):

    # Testing the LRU size with invalid sizes
    def test_lru_size(self):
        with self.assertRaises(ValueError):
            self.lruBad1 = LRU('banana')
            self.lruBad2 = LRU(-5)
            self.assertIsNone(self.lruBad1)
            self.assertIsNone(self.lruBad2)

    # Testing the LRU put
    def test_lru_put(self):
        self.lru.put('1', 'Test Put 1')
        self.lru.put('2', 'Test Put 2')
        self.lru.put('3', 'Test Put 3')
        self.lru.put('4', 'Test Put 4')
        self.assertEqual(self.lru.get("3"), 'Test Put 3')
        self.lru.put('5', 'Test Put 5')
        self.assertEqual(self.lru.get("1"), None)
        self.assertEqual(list(self.lru.cache), self.lru.keys)

    # Testing the LRU get
    def test_lru_get(self):
        check = self.lruFull.get("4")
        self.assertEqual(check, 'Test Get 4')
        self.lruFull.put('5', 'Test Get 5')
        self.assertEqual(self.lruFull.get("1"), None)
        self.assertEqual(self.lruFull.get("1"), None)
        self.lruFull.put('1', 'Test Get 1')
        self.lruFull.put('2', 'Test Get 2')
        self.lruFull.put('3', 'Test Get 3')
        self.lruFull.put('4', 'Test Get 4')
        self.assertEqual(list(self.lruFull.cache), self.lruFull.keys)

    # Testing the LRU maz size
    def test_lru_max(self):
        self.lruFull.put('1', 'Test Get 1')
        self.lruFull.put('2', 'Test Get 2')
        self.lruFull.put('3', 'Test Get 3')
        self.lruFull.put('4', 'Test Get 4')
        self.lruFull.put('5', 'Test Get 5')
        self.lruFull.put('6', 'Test Get 6')
        self.lruFull.put('7', 'Test Get 7')
        self.lruFull.put('8', 'Test Get 8')
        self.assertEqual(self.lruFull.cache_max(), 4)
        self.assertEqual(len(self.lruFull.cache), 4)
        self.assertEqual(len(self.lruFull.keys), 4)

    # Testing the LRU delete
    def test_lru_delete(self):
        self.lruFull.delete('1')
        self.assertEqual(self.lruFull.get("1"), None)
        self.assertNotIn('1', list(self.lruFull.cache))
        self.assertNotIn('1', self.lruFull.keys)

    # Testing the LRU reset
    def test_lru_reset(self):
        self.lruFull.reset()
        self.assertNotIn('1', list(self.lruFull.cache))
        self.assertNotIn('1', self.lruFull.keys)
        self.assertEqual(len(self.lruFull.cache), 0)
        self.assertEqual(len(self.lruFull.keys), 0)
        self.assertEqual(self.lruFull.max, 4)

    # Testing the LRUOD size with invalid sizes
    def test_lruod_size(self):
        with self.assertRaises(ValueError):
            self.lruodBad1 = LRUOD('banana')
            self.lruodBad2 = LRUOD(-5)
            self.assertIsNone(self.lruodBad1)
            self.assertIsNone(self.lruodBad2)

    # Testing the LRUOD put
    def test_lruod_put(self):
        self.lruod.put('1', 'Test Put 1')
        self.lruod.put('2', 'Test Put 2')
        self.lruod.put('3', 'Test Put 3')
        self.lruod.put('4', 'Test Put 4')
        self.assertEqual(self.lruod.get("3"), 'Test Put 3')
        self.lruod.put('5', 'Test Put 5')
        self.assertEqual(self.lruod.get("1"), None)
        self.assertEqual(self.lruod.cache['5'], 'Test Put 5')

    # Testing the LRUOD get
    def test_lruod_get(self):
        check = self.lruodFull.get("2")
        self.assertEqual(check, 'Test Get 2')
        self.lruodFull.put('5', 'Test Get 5')
        self.assertEqual(self.lruodFull.get("1"), None)
        self.lruodFull.put('1', 'Test Get 1')
        self.lruodFull.put('2', 'Test Get 2')
        self.lruodFull.put('3', 'Test Get 3')
        self.lruodFull.put('4', 'Test Get 4')
        self.assertEqual(str(self.lruodFull.cache), "OrderedDict([('1', 'Test Get 1'), ('2', 'Test Get 2'), "
                                                    "('3', 'Test Get 3'), ('4', 'Test Get 4')])")

    # Testing the LRUOD maz size
    def test_lruod_max(self):
        self.lruodFull.put('1', 'Test Get 1')
        self.lruodFull.put('2', 'Test Get 2')
        self.lruodFull.put('3', 'Test Get 3')
        self.lruodFull.put('4', 'Test Get 4')
        self.lruodFull.put('5', 'Test Get 5')
        self.lruodFull.put('6', 'Test Get 6')
        self.lruodFull.put('7', 'Test Get 7')
        self.lruodFull.put('8', 'Test Get 8')
        self.assertEqual(self.lruod.cache_max(), 4)
        self.assertEqual(len(self.lruodFull.cache), 4)

    # Testing the LRUOD delete
    def test_lruod_delete(self):
        self.lruodFull.delete('1')
        self.assertEqual(self.lruodFull.get("1"), None)
        self.assertNotIn('1', list(self.lruodFull.cache))
        self.assertNotIn('1', self.lruodFull.cache.keys())

    # Testing the LRUOD reset
    def test_lruod_reset(self):
        self.lruodFull.reset()
        self.assertNotIn('1', list(self.lruodFull.cache))
        self.assertEqual(len(self.lruodFull.cache), 0)
        self.assertEqual(self.lruodFull.max, 4)
