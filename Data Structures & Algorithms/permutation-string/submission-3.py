class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        fm1 = {}
        for char in s1:
            if char not in fm1:
                fm1[char] = 0
            fm1[char] += 1

        for i in range(0, len(s2)):
            fm2 = {}
            substr = s2[i:i+len(s1)]
            for char in substr:
                if char not in fm2:
                    fm2[char] = 0
                fm2[char] += 1
            
            equal = True
            # print(f"fm1: {fm1}")
            # print(f"fm2: {fm2}")
            for char, freq in fm1.items():
                if char not in fm2:
                    equal = False
                elif fm2[char] != fm1[char]:
                    equal = False
            if equal:
                return True
        
        return False