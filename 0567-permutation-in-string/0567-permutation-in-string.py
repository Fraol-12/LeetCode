class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        if k > len(s2):
            return False
        count1 = Counter(s1)
        window = Counter(s2[:k])

        if window == count1:
            return True
        for i in range(k, len(s2)):
            window[s2[i]] += 1
            left_char = s2[i-k]
            window[left_char] -= 1    

            if window[left_char] == 0:
                del window[left_char]

            if window == count1:
                return True
        return False            