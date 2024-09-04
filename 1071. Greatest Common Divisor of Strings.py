"""
len(1) = 6
len(2) = 3 
len(gcd) = 3

6, 4 - 2

4, 4 - 4
 
Solution: If str1+str2 == str2+str1, then the string GCD has the length of the GCD between the lengths of str1 and str2
- Define fn to get the GCD
- Return the substring of str1 with length GCD

Time complexity: O(n + m) - n, m are the lens of str1, str2 
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ""

        gcd = self.getGCD(len(str1), len(str2))
        return str1[0:gcd]

    def getGCD(self, x, y):
        if x == 0:
            return y
        return self.getGCD(y % x, x)   
        
