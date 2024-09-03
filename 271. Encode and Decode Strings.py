"""
Issue: Can't use a global delimiter such as , because it could exist in the stirng
Solution: Use a delimiter unique to each string. This will be the string length followed by a char indicating the end of the length and beginning of the word.
- Delimiter is x! where x is the string length
- Iterate through the list and concat each string and its delimiter
- Decode this string by reading the length (until the !) and taking the next x chars for the current string
Time complexity: O(n) for encode and decode
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "!" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0

        while i < len(s):
            j = i  # tracks read chars

            while s[j] != "!":
                j += 1
            
            str_len = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+str_len])
            i = j + 1 + str_len

        return decoded_strs
