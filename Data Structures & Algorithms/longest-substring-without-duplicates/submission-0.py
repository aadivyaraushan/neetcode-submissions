class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in output_set:
                # remove duplicates
                while s[right] in output_set:
                    output_set.remove(s[left])
                    left += 1
            
            output_set.add(s[right])
            right += 1
            max_len = max(len(output_set), max_len)

        return max_len
            


        