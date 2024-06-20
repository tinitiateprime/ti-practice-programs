# LRU Cache Implementation
* Implement a Least Recently Used (LRU) cache. The cache should be able to store a fixed number of items, and when the cache exceeds its capacity, it should remove the least recently used item.

# LRU Cache Implementation
This project implements a Least Recently Used (LRU) cache using Python. An LRU cache removes the least recently used item when the cache reaches its capacity.

## Files

- `lru_cache.py`: Contains the main code for the LRU cache implementation.

## Classes
### `LRUCache`
Represents the LRU cache.

#### Methods

- `__init__(self, capacity: int)`
   - Initializes the cache with a fixed capacity.
   - Args:
      - `capacity` (int): The maximum number of items the cache can hold.
   
<li>`get(self, key: int) -> int`


- Retrieves an item from the cache.
- Args:
   - `key` (int): The key of the item to retrieve.

<li>Returns:
- `int`: The value of the item if it exists in the cache, otherwise -1.

<li>Description:
- Returns the value associated with the key if it exists in the cache.
- Moves the accessed item to the end to indicate it was recently used.

<li>`put(self, key: int, value: int) -> None`


- Adds or updates an item in the cache.
- Args:
   - `key` (int): The key of the item.
   - `value` (int): The value of the item.

<li>Description:
- Adds the key-value pair to the cache.
- Moves the existing item to the end to indicate it was recently used.
- Removes the least recently used item if the capacity is exceeded.

## Usage

- Import the `LRUCache` class from the `lru_cache.py` file.
- Create an instance of the `LRUCache` class with a specified capacity.
- Use the `put` method to add items to the cache.
- Use the `get` method to retrieve items from the cache.