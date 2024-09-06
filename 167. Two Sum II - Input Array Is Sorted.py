"""
Solution: Use two pointers at start/end of the list.
- Check the sum of indexes' values against the target
- Equal -> return indexes
- Smaller -> inc start
- Larger -> decr end 

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, end = 0, len(numbers) - 1

        while start < end:
            curr_sum = numbers[start] + numbers[end]

            if curr_sum > target:
                end -= 1
            elif curr_sum < target:
                start += 1
            else:
                return [start + 1, end + 1]
