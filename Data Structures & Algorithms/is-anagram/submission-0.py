class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] = s_map[char] + 1
        for char in t:
            if char not in s_map:
                return False
            s_map[char] = s_map[char] - 1
        for key, value in s_map.items():
            if value != 0:
                return False
        return True