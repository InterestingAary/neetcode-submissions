class Solution:
    def containsNearbyDuplicate(self, nums, k):
        a = set()
        for i,num in enumerate(nums):
          if num in a:
             return True
          a.add(num)
          if len(a) > k:
            a.remove(nums[i-k])
        return False
