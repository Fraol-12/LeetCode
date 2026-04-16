class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int) 
        window_sum = 0
        left = 0
        answer = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            freq[nums[right]] += 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                window_sum -= nums[left] 

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1    

            if right - left + 1 == k:
                if len(freq) == k:
                    answer = max(window_sum, answer)
        return answer
                        
