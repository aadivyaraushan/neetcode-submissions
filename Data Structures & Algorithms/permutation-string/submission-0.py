class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = "".join(sorted(list(s1)))
        for i in range(0, len(s2)):
            s2_substr_sorted = "".join(sorted(list(s2[i: i + len(s1)])))
            print(s2_substr_sorted)
            if s1_sorted == s2_substr_sorted:
                return True
        
        return False
