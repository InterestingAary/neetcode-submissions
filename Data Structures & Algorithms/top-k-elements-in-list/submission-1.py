from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        items = []
        for key in freq:
            items.append((key, freq[key]))


        def get_count(pair):
            return pair[1]

        items.sort(key=get_count, reverse=True)


        result = []
        for i in range(k):
            result.append(items[i][0])

        return result
