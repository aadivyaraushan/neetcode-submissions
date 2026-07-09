class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(path, start, s):
            # print(f"in current call: path = {path}, nums = {nums}, s = {s}")
            nonlocal ans
            if s > target:
                return
            if s == target:
                ans.append(path.copy())
                return
            visited = set()
            # print(f"\n\ncurrently, start = {start}")
            for i in range(start, len(candidates)):
                # print(f"at start of iteration, visited = {visited}")
                num = candidates[i]
                if s + num > target:
                    break

                if num not in visited:
                    path.append(num)
                    # print(f"making path {path}")
                    visited.add(num)
                    # print(f"calling nums from index {i+1} onwards")
                    backtrack(path, i+1, s + num)
                    path.pop()
        # print(f"sorted candidates: {candidates}")
        backtrack([], 0, 0)
        return ans