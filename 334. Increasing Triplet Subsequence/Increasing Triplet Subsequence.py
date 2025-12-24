class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # We track two values:
        # 1. `first`  -> the smallest number seen so far
        # 2. `second` -> the smallest number greater than `first`
        #
        # While iterating:
        # - Update `first` if we find a smaller or equal number
        # - Update `second` if the number is greater than `first`
        #   but smaller or equal to `second`
        # - If we find a number greater than both `first` and `second`,
        #   an increasing triplet subsequence exists
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
