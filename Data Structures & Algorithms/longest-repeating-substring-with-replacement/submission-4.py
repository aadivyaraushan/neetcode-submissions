class Solution:

    def most_freq_char_count(self, s: str):
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        # print(f"freq_map: {freq_map}")
        
        pairs = []
        for key, value in freq_map.items():
            pairs.append((value, key))
        pairs.sort(reverse=True)
        return pairs[0][0]

    def characterReplacement(self, s: str, k: int) -> int:
        # what our loss criterion is
        # if the window has more than one character
        # then its not valid so move ahead

        # and we're tracking
        # length of max window with one distinct character

        max_len = 0
        substr = ""
        left = 0
        set_of_chars = set()
        for right in range(len(s)):
            substr = s[left:right+1]
            # print(f"substr: {substr}")
            # print(f"left = {left} and right = {right}")

            for char in substr:
                set_of_chars.add(char)
            # print(f"new set of chars: {set_of_chars}")
            
            while (len(set_of_chars) > 1 and (len(substr) - self.most_freq_char_count(substr)) > k):
                # this means there is more than one character
                # print(f"there's more than one character in substr")
                left += 1
                # print(f"left becomes {left}")
                substr = s[left:right]
                # print(f"substr becomes: {substr}")
                set_of_chars = set()
                for char in substr:
                    set_of_chars.add(char)
                # print(f"set of chars is now: {set_of_chars}")

            if len(substr) > max_len:
                max_len = len(substr)
                # print(f"updating max len to be: {max_len}")
            # right += 1 happens at end
        return max_len