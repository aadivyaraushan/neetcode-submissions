from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used_capacity = 0
        self.elems = {}
        self.key_usage_queue = deque()

    def update_usage_queue(self, new_key):
        if new_key in self.key_usage_queue:
            self.key_usage_queue.remove(new_key)
        self.key_usage_queue.append(new_key)

    def get(self, key: int) -> int:
        if key in self.elems:
            self.update_usage_queue(key)
            return self.elems[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.elems:
            self.elems[key] = value
            self.update_usage_queue(key)
        else:
            if self.used_capacity + 1 > self.capacity:
                least_recently_used_key = self.key_usage_queue.popleft()
                self.elems.pop(least_recently_used_key)

            self.elems[key] = value
            self.update_usage_queue(key)

            self.used_capacity += 1
        
