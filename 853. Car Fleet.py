"""
Solution: Visualize speeds like linear equations - starting from position and line continues until it reaches the distance. With multiple cars, lines will start to intersect and then those become a fleet with the min speed between them. So, need to track these intersections (which will become a fleet) and track how many groups of fleets
- Initialize a stack (each element in stack will represent a fleet where that element is the first in its fleet)
- Sort array by position (since it's 1 lane and cars can surpass)
- Starting from the end (closest to target), add the current to stack and check if the previous is faster/reaches target first. If so, those become a fleet and pop the added element.
- If it isn't, that is a new fleet. Continue until all elements added
- Return length of stack (# of fleets)

Time complexity: sorting + iteration = O(nlogn)
Space complexity: O(n)
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [[p, s] for p, s in zip(position, speed)]
        fleets = []

        for p, s in sorted(cars)[::-1]:
            fleets.append((target - p) / float(s))

            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:  # collision
                fleets.pop()  # update fleet

        return len(fleets)
