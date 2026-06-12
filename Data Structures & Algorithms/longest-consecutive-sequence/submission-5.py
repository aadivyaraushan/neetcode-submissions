class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        consecutive_subseq_mapping = {}
        consecutive_subseq_mapping_len = {}
        
        nums.sort()
        print(f'sorted nums: {nums}')
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] - nums[i] == 1 or nums[i] == nums[i+1]:
                if nums[i] == nums[i+1]:
                    consecutive_subseq_mapping_len[nums[i]] = 1
                    i += 1
                    continue

                print(f"found a consecutive pair of {nums[i]}, {nums[i+1]}")
                consecutive_subseq_mapping[nums[i]] = [nums[i+1]]
                consecutive_subseq_mapping_len[nums[i]] = 2
                print(f'consecutive_subseq_mapping_len[{nums[i]}] = 2 now')
                key = nums[i]
                i += 1
                while i+1 < len(nums) and (nums[i+1] - nums[i] == 1 or nums[i] == nums[i+1]):
                    if nums[i] == nums[i+1]:
                        i += 1 
                        continue
                    print(f'inspecting pair {nums[i]}, {nums[i+1]}')
                    consecutive_subseq_mapping[key].append(nums[i+1])
                    consecutive_subseq_mapping_len[key] += 1
                    print(f'consecutive_subseq_mapping_len[{key}] = {consecutive_subseq_mapping_len[key]} now')
                    i += 1
            i += 1
        
        print(f'consecutive subseq mapping: {consecutive_subseq_mapping}')

        linked_pairs = []
        for key, value in consecutive_subseq_mapping_len.items():
            linked_pairs.append((value, key))
        linked_pairs.sort(reverse=True)
        
        if not consecutive_subseq_mapping_len:
            return 1

        return linked_pairs[0][0] 
        