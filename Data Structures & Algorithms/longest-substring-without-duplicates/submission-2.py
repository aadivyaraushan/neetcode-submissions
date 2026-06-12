class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # remove duplicates
            while s[right] in output_set:
                output_set.remove(s[left])
                left += 1
            
            output_set.add(s[right])
            max_len = max(right - left + 1, max_len)

        return max_len
            


        