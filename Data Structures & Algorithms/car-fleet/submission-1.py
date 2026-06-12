class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse=True)

        fleet_times = []

        for position, speed in pairs:
            time = (target - position)/speed
            # print (f"for position {position} and speed {speed}, time = {time}")

            if len(fleet_times) == 0:
                # print(f"added initial time: {time}")
                fleet_times.append(time)
            
            if time > fleet_times[-1]:
                # print(f"found time greater than max in fleet_times i.e. {time} so adding")
                fleet_times.append(time)
        
        return len(fleet_times)


        
