class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        t_set = set(t)
        freq_map = {}
        
        for char in t:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        # print(f"t_set: {t_set}")
        substrings = []

        for left in range(len(s)):
            # print (f"New iteration started w/ left: {left}")

            if s[left] in t_set:
                substrings.append(s[left])
                # print (f"{s[left]} is in t_set. it's at index {left} in s")
                # print(f"t_set is currently {t_set}")
                # print(f"remaining characters: {remaining}")
                # iterate from left onwards
                # check from remaining 
                

                for char in t_set:
                    # print(f"in inner loop, inspecting {char}")
                    # iterate through the non-s[left characters]
                    right = left+1
                    # print(f"right is currently: {right}")
                    while right < len(s):
                        # print(f"substr is currently: {s[left:right+1]}")
                        if char in s[left:right+1]:
                            # print(f"{char} is in substr {s[left:right+1]} with left = {left} and right = {right}")
                            substrings.append(s[left:right+1])
                            # print(f"substrings is now: {substrings}")
                        right += 1
                    
                        
            # find max length substring
            # if output is empty, make output = substring
            # otherwise if output length is lower than max lenth substr 
            # set o/p to that max length substr
            # filter array for strings that don't contain every character in t
            # print(f"before filtering, t_set = {t_set}")
            print(f"before filtering, substrings = {substrings}")
            for char in t_set:
                # print(f"filtering substrings by {char}")

                for substr in substrings.copy():
                    # print(f"seeing if {char} is in {substr}")
                    if char not in substr:
                        # print(f"{char} is not in substr {substr} so removing")
                        substrings.remove(substr)
            # print(f"before filtering by frequency, substrings={substrings}")

            # filtering by frequency
            # print(f"frequency filtering step")
            # print(f"before any filtering, substrings = {substrings}")
            for char, freq in freq_map.items():
                # print(f"filtering for character {char} that has frequency {freq}")
                for substr in substrings.copy():
                    # print(f"seeing if {substr} has {char} at right frequency {freq} ")
                    if substr.count(char) < freq:
                        # print(f"{substr} does not have {char} with frequency {freq} so we're removing it")
                        substrings.remove(substr)
                        # print(f"substrings is now: {substrings}")

            min_length_substr = min(substrings, key=len, default="")
            # print(f"chose min length substr: {min_length_substr}")


            if output == "":
                # print(f"output is an empty string so we automatically make it {min_length_substr}")
                output = min_length_substr
            elif len(output) > len(min_length_substr):
                # print(f"output length is higher than min length substr so we make it {min_length_substr}")
                output = min_length_substr
            
        

        return output