class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # example walkthrough
        # [[1, 2, 3], [7, 1, 1]], target = [7, 2, 3]
        # index 0 -> max of triplets[0], triplets[1] = 7, minimum for 1, 2, 3 = 1, 2, 3
        # Q: do any match? if so check 
        # index 1 -> max of triplets[0], triplets[1] = 2
        # index 2 -> max of same = 3
        # [[2, 5, 6], [1, 4, 4], [5, 7, 5]], target = [5, 4, 6]
        # index 0 -> max = 5, min = 5, 7, 5 -> not possible because targets larger
        # index 1 -> 

        # example 2 walkthrough
        # index 0 -> 5 matches, but 7, 5 dont -> False

        # other variables involved:
        # 1. content of triplets
        # 2. target
        # 3. number of triplets
        # 4. number of swaps involved

        # example:
        # target = 7, 5, 6
        # triplets = [[1, 2, 3], [7, 1, 1], [1, 5, 6]]
        # 0 -> 7 matches, min is < target so okay
        # 1 -> 5 matches, 6 <= 6 so its okay
        # 2 -> 6 matches, no check necessary

        
        # state
        # whats the minimum info i need to get to the answer at any point?
        # -> just based on the values no need to store state i think 
        # index 0 -> 5 -> 5

        # algorithm
        # 1. do any of the values at i in any of the triplets match
        # 2. for that match, from i+1 onwards, are the other values of the triplet <= the other values in the target
        # 3. if so, nothing and just continue
        # 4. if not, return False merge is impossible
        # return True at end

        for i in range(3):
            triplet_match_i = -1
            found = False
            for triplet_i, triplet in enumerate(triplets):
                
                # print(f"inspecting {i} at {triplet} ")
                if triplet[i] == target[i]:
                    triplet_match_i = triplet_i
                    # print(f"potential match at index {triplet_i}")
                    # found a match, inspecting others to see if it works
                    works = True
                    for j in range(0, 3):
                        # print(f"comparing {triplets[triplet_match_i][j]} and {target[j]}")
                        if triplets[triplet_match_i][j] > target[j]:
                            works = False
                            break
                    
                    if works:
                        found = True
                        break
            if not found:
                return False

            
            # print(f"for i: {i}, found triplet match i = {triplet_match_i}")

            if triplet_match_i == -1:
                return False
            
        
        return True

 