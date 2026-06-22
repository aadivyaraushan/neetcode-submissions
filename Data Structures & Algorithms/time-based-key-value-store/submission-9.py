class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        timestamps = self.time_map[key]
        # print(f"timestamps: {timestamps}")
        left = 0
        right = len(timestamps)

        max_timestamp_val = ""
        found = False 
        # print("NEW CALL")
        # print(f"inputs: key = {key} and timestamp = {timestamp}")
        # print(f"starting with time map = {timestamps}")
        # print(f"starting with left = {left} and right = {right}")
        

        while left < right:
            mid = (left + right) // 2
            if mid >= len(timestamps):
                break
            ts = timestamps[mid][0]
            # print(f"ts: {ts}")
            # print(f"mid: {mid} and ts = {ts}")

            if timestamp >= ts:
                max_timestamp_val = timestamps[mid][1]
                found = True
                left = mid + 1
                # print(f"left is now {left} while right is {right}")
            else:
                right = mid 
                # print (f"moving left since not found, right becomes {right}")
        
        # print(f"returning {max_timestamp_val}")
        if not found:
            return ""
        return max_timestamp_val

            
