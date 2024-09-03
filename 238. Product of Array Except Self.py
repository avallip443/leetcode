"""
Solution: Since division can't be used (i.e. find the product of all element and divide by each element for the specific output value), multiplying the prefix product by the suffix product will produce the output.
- Could use two arrays for storing the prefix/suffix for each index. Then for the nth value, use the n-1 prefix value and n+1 suffix value (default 1 for out of bound values) to get the product. However, this would take O(n) space.
- Can use O(1) space by using the output array to store the prefix/suffix values (where the prefix/suffix would be in the nth position for the nth element).

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [1] * len(nums)

        prefix = 1  
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
