class Solution:

    def compute_hours(self, piles, k) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # inputs:
        # piles = [] -> piles[i] is # of bananas in i'th pile
        # h = number of hours you have to eat all the bananas
        # output = k = bananas-per-hour eating rate
        # each hour, can choose one pile and eat k bananas from that pile
        # if the pile has les than k bananas, you may finish eating the pile
        # but you can't eat from another pile in the same hour


        # dry run with a minimum k
        # for piles = [1, 4, 3, 2], k = 2
        # reason: 
        # hour 1 -> 1
        # hour 2 -> 2nd one half
        # hour 3 -> 2nd one half
        # hour 4 -> 3rd one 2
        # hour 5 -> 3rd one 1 
        # hour 6 -> 4th one 1
        # so 6

        # steps of algo:
        # 1. initial hours = sum of all vals 
        # 2. if hours > h: k += 1
        # 3. if hours < h: k -= 1
        # 4. if hours == h: return k
        # 5. compute hours again w new k

        low_k = 1
        high_k = max(piles)
        min_k = high_k
        while low_k <= high_k:
            # print(f"low_k: {low_k}, high_k: {high_k}")
            k = (low_k + high_k) // 2
            # print(f"k: {k}, current min_k: {min_k}")
            hours = self.compute_hours(piles, k)
            # print(f"hours: {hours}")
            # invariant: eventually this should circle back to the same k at least once
            if hours <= h:
                if min_k == k: 
                    return k
                else:
                    min_k = min(min_k, k)
                    high_k = k 
            elif hours > h:
                low_k = k + 1
            hours = self.compute_hours(piles, k)
        
        
        
