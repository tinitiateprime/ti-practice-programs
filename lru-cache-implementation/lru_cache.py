from collections import OrderedDict

class LRUCache:
    """
    Implementation of Least Recently Used (LRU) cache.
    It is a type of cache that removes the least recently used item when the cache reaches its capacity.
    """
    def __init__(self, capacity: int):
        """
        Initialize the cache with a fixed capacity.
        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        # Initialize the cache with a fixed capacity
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieve an item from the cache.
        Args:
            key (int): The key of the item to retrieve.
        Returns:
            int: The value of the item if it exists in the cache, otherwise -1.
        """
        if key not in self.cache:
            return -1  # Return -1 if the key is not found
        # Move the accessed item to the end to indicate it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Add or update an item in the cache.
        Args:
            key (int): The key of the item.
            value (int): The value of the item.
        """
        if key in self.cache:
            # Move the existing item to the end to indicate it was recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used item if the capacity is exceeded
            self.cache.popitem(last=False)

# Example usage:
cache = LRUCache(2)
cache.put(1, 1)  # Cache is {1=1}
cache.put(2, 2)  # Cache is {1=1, 2=2}
print(cache.get(1)) # returns 1 and moves key 1 to the end: Cache is {2=2, 1=1}
cache.put(3, 3)    # Evicts key 2: Cache is {1=1, 3=3}
print(cache.get(2)) # returns -1 (not found)
cache.put(4, 4)    # Evicts key 1: Cache is {3=3, 4=4}
print(cache.get(1)) # returns -1 (not found)
print(cache.get(3)) # returns 3
print(cache.get(4)) # returns 4