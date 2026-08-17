class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        largest = hand[-1]
        freq_map = {}
        for elem in hand:
            if elem not in freq_map:
                freq_map[elem] = 0
            freq_map[elem] += 1
        

        # print(f"post init, freq map = {freq_map}")
        
        while True:
            found_start = False
            smallest_unused = 0
            for card, freq in freq_map.items():
                # print(f"inspecting card: {card}, freq: {freq} ")
                if freq > 0:
                    found_start = True
                    smallest_unused = card
                    break
                if freq < 0:
                    return False
            if not found_start:
                break
            
            for i in range(smallest_unused, smallest_unused + groupSize):
                if i not in freq_map:
                    return False
                freq_map[i] -= 1
        
        return True
            