"""
Solution: Use fixed sliding window. First initalize count for first window and set it to the max. Then iterate from the kth pos and adjust the count based on the new window (add if new is vowel, subtract is last is vowel). Return max

TIme complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = 'aeiou'
        count = sum(1 for i in s[:k] if i in vowels)
        max_count = count

        for i in range(k, len(s)):
            count += 1 if s[i] in vowels else 0
            count -= 1 if s[i-k] in vowels else 0

            max_count = max(max_count, count)
        
        return max_count
