class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for string s
        # This tracks which character of s we are trying to match
        left = 0

        # Loop through each character in t
        for char in t:
            # If all characters in s are already matched, we can stop
            if left == len(s):
                break

            # If current characters match, move the pointer in s forward
            if s[left] == char:
                left += 1

        # If we have matched all characters in s,
        # then s is a subsequence of t
        return left == len(s)
