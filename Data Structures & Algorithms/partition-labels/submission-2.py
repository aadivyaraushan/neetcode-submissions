class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # decision at every point -> should i open new substring or continue new one?
        # what determines? whether we've covered all occurrences in the string of the characters in that substring
        # (so that it doesn't show up in other substrings)
        # in term of state -> iterate through each char in substr chars, if freq_map[that char] is not 0
        # for any of them, that means we havent covered (can keep flag "covered" for this)
        # if we have, move on and start new substring
        # in terms of state -> set substr chars to empty, 
        # if we haven't, continue w current substring
        # in terms of state -> add this char to substr chars,

        # what's the minimum state required to figure that out?
        # 1. freq map of characters to see if we've covered all (figured out using freq_map[char])
        # 2. set storing current substr chars
        # 3. char storing current char we're iterating htrough in s
        
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        
        i = 0
        lengths = []
        substr_chars = set()
        length = 0
        for char in s:
            covered = True
            for substr_char in substr_chars:
                if freq_map[substr_char] != 0:
                    covered = False
                    break
            
            if covered and len(substr_chars) > 0:
                lengths.append(length)
                substr_chars = set(char)
                freq_map[char] -= 1
                length = 1
            else:
                freq_map[char] -= 1
                substr_chars.add(char)
                length += 1
        lengths.append(length)

        return lengths



