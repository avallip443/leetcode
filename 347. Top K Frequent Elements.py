"""
Initial plan: Use hashmap to map each element to its occurances. Get the list of values and get the k most frequent keys, but getting those keys will be complex.

Solution: Map the number of occurances to a list of elements with that many occurances and return the k more frequent elements
- Use hashmap to map each element to its occurances
- Use nested list to map the occurances from 1 to n to each element
- Iterate nested list in reverse to get the k most frequent elements
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
        
        my_hash = {}
        occurances = [[] for i in range(len(nums) + 1)]

        for num in nums:
            my_hash[num] = 1 + my_hash.get(num, 0)

        for num, count in my_hash.items():
            occurances[count].append(num)  # append num to list with count occurances

        res = []
        for i in range(len(occurances) - 1, 0, -1):  # iterate from most to least occurances
            for j in occurances[i]:
                res.append(j)
                if len(res) == k:  
                    return res
