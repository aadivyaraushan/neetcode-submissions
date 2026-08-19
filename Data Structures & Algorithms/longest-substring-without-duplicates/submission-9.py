class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # how would i solve this myself?
        # sliding window clearly
        # zxyzxyz
        # no duplicate characters
        # start at z
        # add x. no duplicate so ok.
        # add y. no duplicate so ok.
        # add z. now duplicate detected so
        # remove from left -> or rather keep removing till
        # no duplicates


        # print(f"has_duplicates: {has_duplicates("abc")}")


        # what if it iwa s like zxyx
        # once we add x youd have to remove two of them
        # yeah got it
        # ^ this doesnt lose info cuz the main thing we care about
        # the max len
        # would alr have been recorded in the prior iteration
        if len(s) == 0:
            return 0
        max_len = 1
        l = 0
        chars = set(s[l])
        for r in range(1, len(s)):
            # print(f"starting iteration w/ l  = {l} and r = {r}, chars = {chars}")
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            else:
                # print(f"added {s[r]} to chars making it {chars}, l = {l}, r = {r}")
                max_len = max(max_len, r-l+1)
            chars.add(s[r])
        
    
        return max_len


