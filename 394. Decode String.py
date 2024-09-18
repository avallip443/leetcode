"""
Solution: Since encoded sequences can be nested in each other and must be done linearly, can use stack to track current number and string being decoded (order is [num, str, ...]).

4 possible outputs - number, char, [, and ]. 
- Number encountered -> check with is isdigit(). To handle numbers > 10, multiple the current num var by 10 (eg. 3 -> 30) and add the current value (eg. 30 + 1)
- [ encountered -> push curr num/str to stack (new string has to be decoded) and reset vars
- ] encountered -> pop previous num and str and add the decoded sequence to the curr str. This also handles nested encoded sequences (eg. 3[a2[b]])
- char encountered -> add to curr str

At the end, prepend any remaining chars

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_str = ""
        curr_num = 0

        for c in s:  
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + (curr_str * prev_num) 
            else:  # char 
                curr_str += c
        
        while stack:  # handle remaining chars 
            curr_str = stack.pop() + curr_str
        
        return curr_str
