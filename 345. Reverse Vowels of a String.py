"""
Solution: Use two pointer to track the beginning/end of the str and its vowel.
- Convert the string to an array
- When the points reach a vowel, swap the chars at those position
- Repeat until pointers cross
- Return array as string

Time complexity: O(n)
Space complexity: O(n) - new array for word

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        word = list(s)
        i, j = 0, len(s) - 1
        vowels = "aeiouAEIOU"

        while i < j:
            while i < j and vowels.find(word[i]) == -1:
                i += 1
            
            while i < j and vowels.find(word[j]) == -1:
                j -= 1
                
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        
        return "".join(word)
            
