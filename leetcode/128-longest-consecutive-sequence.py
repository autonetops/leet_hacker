# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import Counter
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))

        max_consecutive_length = 1
        length = 1
        if not nums:
            return 0
        for i in range(len(sortedNums)):
            if i == 0:
                continue

            if sortedNums[i] - sortedNums[i - 1] == 1:
                length += 1
            else:
                length = 1

            max_consecutive_length = max(max_consecutive_length, length)
        return max_consecutive_length


longestConsecutive = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
