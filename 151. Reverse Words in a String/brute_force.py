# the string may have leading spaces, trailing spaces, or multiple spaces
# words are defined as non-space characters
# the goal is to reverse the order of words and return them with one space only

# approach
# split the string by spaces (this may create empty strings)
# remove empty strings and keep only valid words
# reverse the list of words
# join the words using a single space
# return the final string

class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        valid_words = []

        for word in words:
            if word != "":
                valid_words.append(word)

        valid_words.reverse()
        return " ".join(valid_words)


# time complexity = O(n)
# space complexity = O(n)
