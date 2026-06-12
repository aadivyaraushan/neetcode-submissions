class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 0
            
            frequency_map[num] = frequency_map[num] + 1
        
        sorted_pairs = []

        for key, value in frequency_map.items():
            sorted_pairs.append((value, key))
        
        sorted_pairs.sort(reverse=True)

        output = []

        i = 0
        for key, value in sorted_pairs:
            if i == k:
                break
            output.append(value)
            i = i + 1
        
        return output