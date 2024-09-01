#Innehåller implementationen av en LRU-cache (Least Recently Used cache), som används för att optimera prestandan när data hämtas flera gånger.
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        # Returnerar None om nyckeln inte finns
        if key not in self.cache:
            return None
        # Flyttar den använda posten till slutet (senast använd)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value):
        # Om nyckeln redan finns, flytta till slutet för att markera den som senast använd
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # Om cachen överstiger sin kapacitet, ta bort den äldsta posten
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Skapa en LRU-cache med plats för 50 personer
lru_cache = LRUCache(50)
