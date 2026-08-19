class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for position, speed in cars:
            time = (target - position)/speed
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        

        # simulation:
        # 0th car -> starts at 1, speed 3
        # 1st car -> starts at 4, speed 2
        # outcome: # of car fleets
        # car fleet = set of cars driving at same position at same speed
        # how its formed: 
        # 0 goes from 1 -> 4 -> 7 -> 10
        # 1 goes from 4 -> 6 -> 8 -> 10 (forms a fleet, reached at same time)
        # time for both = 4 
        # ex 2
        # 4 -> 6 -> 8 -> 10 -> t = 4
        # 1 -> 3 -> 5 -> 7 -> 9 -> 11
        # 0 -> 1 -> so on -> 10
        # 7 -> 8 -> 9 -> 10 -> t = 4
