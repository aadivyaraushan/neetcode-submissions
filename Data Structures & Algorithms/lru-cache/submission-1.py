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
            # if in elems, return and add to recently used
            self.update_usage_queue(key)
            # print(f"after get, key usage queue = {self.key_usage_queue}")
            return self.elems[key]
        else:
            # if not in elems, return -1
            return -1

    def put(self, key: int, value: int) -> None:
        # if key is in elems, update value of key and add key to recently used
        if key in self.elems:
            self.elems[key] = value
            self.update_usage_queue(key)
            # print(f"after put, key usage queue = {self.key_usage_queue}")
        else:
            # if key isn't in elems, first check if new cap is higher
            if self.used_capacity + 1 > self.capacity:
                # if so then access the least recently used key from the deque
                # and then remove that elem from the map
                least_recently_used_key = self.key_usage_queue.popleft()
                # print(f"about to exceed capacity")
                # print(f"least recently used key = {least_recently_used_key}")
                self.elems.pop(least_recently_used_key)
                # print(f"elems after removal is: {self.elems}")

            # and then add htis this key
            self.elems[key] = value
            self.update_usage_queue(key)

            # update used capacity and increase by 1
            self.used_capacity += 1
            # invariant: should correctly represent used capacity
            # print(f"now, capacity = {self.capacity} while used capacity = {self.used_capacity} and elems = {self.elems}")
            # print(f"after put, key usage queue = {self.key_usage_queue}")
            
