"""
Solution: Use bucket sort. First use hash to get counts of characters, then use an array to sort elements by their occurances (eg. i=1 means ith position has elements with 1 occurance).
- Iterate backwards to get k most frequent.

Time complexity: O(n)
Space complexity: o(n)

"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        res= []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for i, v in count.items():
            frequency[v].append(i)
        
        for i in frequency[::-1]:
            for j in i:
                res.append(j)

                if len(res) == k:
                    return res
        
