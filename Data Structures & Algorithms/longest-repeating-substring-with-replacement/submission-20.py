class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}

        # in sliding windwo here
        # ideal k = when windowSize - most freq element freq
        # if ideal k > k then invalid
        # if invalid then keep moving l and adjusting freq map accordingly (by removing counts of l)
        # until window size - most freq elem freq = 0
        
        # algorithm steps:
        # 1. iterate through each r 
        # 2. at a given r, update frequency map with value
        # 3. now, if window size - freq of most freq element is > k then window is invalid so
        # a. starting from current l, keep removing s[l] from freq map and doing l += 1 till windowSize - freq of most freq element = 0
        # 4. otherwise, window is valid so just continue no change
        l = 0
        longest_len = 0
        for r in range(0, len(s)):
            if s[r] not in freq_map:
                freq_map[s[r]] = 0
            freq_map[s[r]] += 1
            largest = sorted(freq_map.values())[-1]
            window_size = r - l + 1
            # print(f"l = {l}, r = {r}, freq_map = {freq_map}")
            # print(f"window size: {window_size}, largest = {largest}")
            if window_size - largest > k:
                # invalid so minimize
                # print(f"starting to minimize because invalid")
                while True:
                    freq_map[s[l]] -= 1
                    # print(f"changed freq map to {freq_map}")
                    l += 1
                    # print(f"l is now {l}. freq_map.values(): {freq_map.values()}")
                    largest = sorted(freq_map.values())[-1]
                    # print(f"largest: {largest}")
                    if r - l + 1 - largest <= k:
                        break
            else:
                longest_len = max(longest_len, r-l+1)
                # print(f"setting longest len to {longest_len}")
        
        return longest_len
            


