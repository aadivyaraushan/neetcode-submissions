class Solution:

    

    def minWindow(self, s: str, t: str) -> str:
        def add_char_to_freq_map(char, freq_map):
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        def remove_char_from_freq_map(char, freq_map):
            freq_map[char] -= 1
            if freq_map[char] == 0:
                del freq_map[char]

        def does_a_contain_b(freq_map_a, freq_map_b):
            # INVARIANT: does_a_contain_b should return true if w/ th freq map logic a contains the characters of b

            for char, freq in freq_map_b.items():
                # INVARIANT: should run through all characters inf req_map_b
                # print(f"checking {char} which has freq {freq}")
                if char not in freq_map_a:
                    # print (f"{char} isn't in substr")
                    return False
                if freq > freq_map_a[char]:
                    # print (f"{char}'s frequency in t is greater than char's frequency in substr")
                    return False
            
            return True
        
        output = ""
        min_substrings = []
        
        step = 0

        left = 0
        right = 1

        substr_freq_map = {s[0]: 1}
        # INVARIANT: substr freq map should be updated at each point where the substr is enlarged
        # that means:
        # 1. else statement where right += 1
        # 2. expansion inside minimization sequence when can minimize
        # 3. expansion isnide minimization sequence when can't minimize

        t_freq_map = {}
        for char in t:
            add_char_to_freq_map(char, t_freq_map)
        
        while right < len(s) + 1:
            # INVARIANT: left < right always
            # check if valid
            substr = s[left:right]

            # INVARIANT: does_a_contain_b should return true if w/ th freq map logic a contains the characters of b
            if does_a_contain_b(substr_freq_map, t_freq_map):
                original_left = left # storing original_left to reset pos once found a substr
                # INVARIANT: original_left shouldn't get updated in the loop

                # print(f"valid substring found: {substr}. moving forward to miniimze")
                min_substrings.append(substr)
                while True:
                    # INVARIANT: at least left or right should move in one of the versions of this 
                    # EXPECTATION: left, right change 
                    # print(f"left: {left}, right: {right}")


                    temp_left = left + 1
                    new_substr = s[temp_left:right]
                    new_substr_freq_map = substr_freq_map
                    # add_char_to_freq_map(s[temp_left], new_substr_freq_map)
                    # INVARIANT: new_substr_freq_map should corespond to new_substr
                    # print(f"new_substr = {new_substr} and new_substr_freq_map = {new_substr_freq_map}")

                    remove_char_from_freq_map(s[left], new_substr_freq_map)
                    # INVARIANT: substr_freq_map should always correspond to substr
                    # print(f"new substr: {s[temp_left:right]} and new_substr_freq_map = {new_substr_freq_map}")


                    if does_a_contain_b(new_substr_freq_map, t_freq_map):
                        # print(f"s[left]: {s[left]}")
                        substr_freq_map = new_substr_freq_map
                        left = temp_left
                        substr = new_substr

                        # INVARIANT: substr_freq_map should always correspond to substr
                        # print(f"in if: new substr: {s[temp_left:right]} and new_substr_freq_map = {new_substr_freq_map}")

                    else:
                        # exit condition
                        # substr is the last valid string
                        # INVARIANT: substr should always hold the last iteration's string
                        min_substrings.append(substr)
                        left = original_left + 1 
                        right = left + 1 
                        new_freq_map = {}
                        for char in s[left:right]:
                            add_char_to_freq_map(char, new_freq_map)
                        substr_freq_map = new_freq_map
                        # INVARIANT: this should not cover any ground that hasn't already been covered
                        # INVARIANT: the way substr is set up here should trigger further exploration
                        # print (f"now substr would start with: {s[left: right]} with substr_freq_map = {substr_freq_map}")
                        break
                        
                    # step += 1

                    # if step > 25:
                        # print("ENTERING INFINITE LOOP BREAKING")
                        # break
            else:
                # print (f'right increasing now: {right} -> {right + 1}')
                if right < len(s):
                    add_char_to_freq_map(s[right], substr_freq_map)
                right += 1
                

                # INVARIANT: substr_freq_map should always correspond to substr
                # print(f"new substr: {s[left:right]} and substr_freq_map = {substr_freq_map}")
            # if step > 25:
                # print("ENTERED INFINITE LOOP BREAKING")
                # break
        
        return min(min_substrings, key=len, default="")