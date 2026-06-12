class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        # map of sorted strings to the strings that are all anagrams

        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            
            anagram_map[sorted_str].append(string)
        
        output_arr = []
        
        for _, string_array in anagram_map.items():
            elem = []
            for string in string_array:
                elem.append(string)
            
            output_arr.append(elem)
        return output_arr
            

