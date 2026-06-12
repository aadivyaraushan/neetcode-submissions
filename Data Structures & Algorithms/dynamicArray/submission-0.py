class DynamicArray:
    
    def __init__(self, capacity: int):
        # print(f"set capacity to {capacity}")
        self.capacity = capacity
        self.array = []
        # print(f"array is: {self.array}")


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(n)
        # print (f"added {n} to end")
        # print(f"array is now: {self.array}")
        # print (f"capacity is now: {self.capacity}")

    def popback(self) -> int:

        # print (f"capacity is now: {self.capacity}")
        # print(f"last element: {self.array[capacity]}")
        elem = self.array[len(self.array) - 1]
        self.array.pop()
        return elem

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        # print (f"capacity is now: {self.capacity}")

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
