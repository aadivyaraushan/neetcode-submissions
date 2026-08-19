class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = {}
        for char in s1:
            if char not in f1:
                f1[char] = 0
            f1[char] += 1
        l = 0
        f2 = {}
        for r in range(0, len(s2)):
            # 1. add s2[r] to f2
            if s2[r] not in f2:
                f2[s2[r]] = 0
            f2[s2[r]] += 1

            # 2. if s2 substr is too large, make it smaller to len 3
            if r - l + 1 > len(s1):
                f2[s2[l]] -= 1
                if f2[s2[l]] == 0:
                    f2.pop(s2[l])
                l += 1

            # 3. check if s2 substr = f1 map if so eq if not continue
            equal = True
            for char, freq in f1.items():
                if char not in f2:
                    equal = False
                elif f2[char] != f1[char]:
                    equal = False
            if equal:
                return True

        return False
