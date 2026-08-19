class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_time = 0

        for position, speed in cars:
            time = (target - position) / speed

            if time > slowest_time:
                fleets += 1
                slowest_time = time
        return fleets