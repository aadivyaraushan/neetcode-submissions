class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        current_start = 0
        current_gas = 0
        i = 0
        journey_count = 0
        visited_starts = set()

        while True:
            if journey_count == len(gas):
                return current_start
            if len(visited_starts) == len(gas):
                return -1

            current_gas += gas[i]
            current_gas -= cost[i]

            if current_gas < 0:
                visited_starts.add(current_start)
                current_start = (i+1) % len(gas)
                journey_count = 0
                current_gas = 0
            else:
                journey_count += 1

            i = (i + 1) % len(gas)
        