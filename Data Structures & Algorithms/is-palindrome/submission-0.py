class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_parsed = ""
        for char in s:
            if char.isalnum():
                s_parsed += char.lower()
        print(s_parsed)
        return s_parsed == s_parsed[::-1]