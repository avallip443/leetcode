"""
Solution: Find the max fron the candies array, then create a new bool array if extraCandies + max >= candies[i]

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max_candies = 0
        res = []
        
        for kid in candies:
            max_candies = max(max_candies, kid)

        for i in range(len(candies)):
            res.append(candies[i] + extraCandies >= max_candies)

        return res
        
        
