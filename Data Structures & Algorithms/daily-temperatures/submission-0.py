class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            print(f"i: {i} and at {temperatures[i]}")
            # if j has temp > temp[i], set results[i] to j - i
            # otherwise, increase j
            # this gets us the value for results[i]
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    results[i] = j - i
                    break

        return results