class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = float('inf')
        for num in nums:
            if abs(num) < abs(distance):
                distance = num
            elif abs(num) == abs(distance):
                # have different signal
                if distance ^ num < 0:
                    distance = abs(num)
                else:
                    distance = num

        return distance                 