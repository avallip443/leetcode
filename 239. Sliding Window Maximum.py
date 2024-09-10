"""
Solution: Use deque to store max values encountered and to have is sorted in decreasing value to quick access to leftmost and rightmost.
- Initalize res, deque (stores indexes), and window points (0)
- Iterate through nums and add the current index if its value is less than the rightmost one's. Pop values until this is true.
- If the current left index is greater than the leftmost index in the queue (old max), remove it since it's not in the window
- Since r, l = 0, to ensure window is size k, check if r + 1 >= k. If so, add the leftmost (most) and increment left pointer

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        q = collections.deque()  # stores index
        l = r = 0  # window ptrs

        while r < len(nums):
            # rightmost must be larger than curr to keep decreasing order
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left if out of bounds
            if l > q[0]:
                q.popleft()

            # check window size 
            if (r + 1) >= k:
                # add rightmost (window max)
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
