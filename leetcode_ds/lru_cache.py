"""
Create an LRU cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Leetcode link
https://leetcode.com/problems/lru-cache/description/

"""
from collections import OrderedDict

class LRUCache(OrderedDict):
    """
    class that implements an LRU Cache
    """
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        """
        Get the value from LRUCache
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        Put the value into LRUCache
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(5)
obj.put("a", 14)
param_1 = obj.get("a")
print(param_1)
