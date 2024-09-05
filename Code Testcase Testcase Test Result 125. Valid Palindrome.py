"""
Solution: Use 2 pointers to track the start and end of the string. 
- Increment start pointer until it reaches a char within the a-z/0-9 ASCII range and decrement the end pointer until it does the same
- Compare the pointers' chars and return false if they are not equal
- For all comparisons/accesses, use the lower() fn to get the lowercase

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1

        valid_range = range(97, 123) + range(48,58)


        while i < j:
            while i < j and ord(s[i].lower()) not in valid_range:
                i += 1
            
            while i < j and ord(s[j].lower()) not in valid_range:
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
    
