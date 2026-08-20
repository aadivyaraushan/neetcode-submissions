class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # how would i solve this myself?
        # [[1, 3], [4, 6]]
        # new interval's [0] (2) < 3 (prev 1) and new interval's 1 (5) < next 6 (next 1)
        # so then we can put it between those
        # why do we merge here? because 

        res = []
        i = 0
        newIntervalAdded = False
        for i in range(len(intervals)):
            curr = intervals[i]
            # print(f"at iteration {i}, curr = {curr}, newInterval = {newInterval}")
            # case 1: current interval behind new interval
            if curr[1] < newInterval[0]:
                res.append(curr)
            elif curr[0] > newInterval[1]:
                # case 2: current is ahead of new interval 
                if not newIntervalAdded:
                    res.append(newInterval)
                    newIntervalAdded = True
                res.append(curr)
            else:
                # case 3: overlapping
                newInterval = [min(newInterval[0], curr[0]), max(newInterval[1], curr[1])]
        if newInterval not in res:
            res.append(newInterval)

        return res

        # manual walkthrough
        # res = []
        # intervals = [[1, 3], [4, 6]]
        # newInterval = [2, 5]
        # first, [1, 3], [2, 5] overlap so make it [1, 5]
        # then, [1, 5], [4, 6] overlap so make it [1, 6]
        # then, at end
        # new inteval isnt in res so add it then rerturn

        # [1, 2] [3, 5], [9, 10]
        # new interval = [6, 7]
        # [1, 2] < [6, 7] 
        # so res = [[1, 2]] we add it
        # [3, 5] < 
        # oh wait so you only add this the moment that 