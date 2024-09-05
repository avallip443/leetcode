"""
Orignal: Iterate over nums (exct for the last 2) and check if 1st < 2nd and 2nd < 3rd. Problem is that elements accessed up to 3 times so can be more efficient

More optimized: Set first, second to inf, then iterate through nums. Check if current num <= first (start new seq) and then if current num <= second (start new seq again). If both conditions fail, then there are is an increasing triplet.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        NOTE: elements checked up to 3 times
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] and nums[i+1] < nums[i+2]:
                return True
        return False
        """

        first = second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
                
