"""
Solution: Iterate over array and check if current, prev, and next position are 0. If so mark curr as 1 and decrement n. At the end, return if n == 0

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
               flowerbed[i] = 1
               n -= 1

               if n == 0:
                return True
        
        return n == 0

        
