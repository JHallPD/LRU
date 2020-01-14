#LRU
Simple LRU & LRU with OrderedDict scripts
### Overview
 Originally Created the LRU using a list & dict. 
 Then updated the code to use an OrderedDict. 
 The LRU is set up using a list & dict to keep track of the order.
 The LRUOD uses a reversed order with 0 being the least recently used.

#### Run Scripts
Requires Python3
    
    python LRU.py
    python LRUOD.py

#### testing
    python -m unittest

#### LRU & LRUOD Commands
    .get(key): get a value and move it to the top of the cache
    .put(key, value): add a variable to the top of the cache
    .reset(): clear the cache completely
    .delete(key): remove specified Key & value, no-op returns None
    .cache_max(): quick check for cache max size
    .print(): print cache contents
    
