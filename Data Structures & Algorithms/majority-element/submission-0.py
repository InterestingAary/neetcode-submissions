from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = []
        for i in range(len(nums)):
            c.append(nums.count(nums[i]))
        return nums[c.index(max(c))]
