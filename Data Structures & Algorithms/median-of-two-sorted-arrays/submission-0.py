from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        nums3 = sorted(n)
        
        length = len(nums3)
        if length % 2 == 0:
            median = (nums3[length // 2] + nums3[length // 2 - 1]) / 2
        else:
            median = nums3[length // 2]
        
        return median
