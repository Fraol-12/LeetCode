# the string may contain extra spaces anywhere
# we scan the string from right to left
# every time we find a word, we add it to the result
# spaces are handled manually so no extra spaces appear

# approach
# start from the end of the string
# skip spaces until a character is found
# mark the end of the word
# move left until a space or start of string is found
# extract the word and add it to result
# repeat until the start of the string
# join collected words with a single space

class Solution(object):
    def reverseWords(self, s):
        result = []
        i = len(s) - 1

        while i >= 0:
            # skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            end = i

            # move to the start of the word
            while i >= 0 and s[i] != " ":
                i -= 1

            start = i + 1
            result.append(s[start:end + 1])

        return " ".join(result)


# time complexity = O(n)
# space complexity = O(n)   (output space only)
