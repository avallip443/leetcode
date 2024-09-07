"""
Solution: Use pointers i, j set to n-1, m-1 and k pointer set to n + m -1.
- i, j track the numbers that need to be merged in nums1, nums2
- k tracks the position to merge into
- Iterate over elements in nums2, compare the values at i/j, place the large into position k, and decr i/j 
- If all nums2 elements are merge, then nums1 is automatically sorted

Time complexity: O(n + m)
Space complexity: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
