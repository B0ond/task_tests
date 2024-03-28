class Solution:
    def two_sum(self, nums, target):
        temp = {}
        for id, num in enumerate(nums):
            compliment = target - num
            if compliment in temp:
                return [temp[compliment], id]
            temp[num] = id
        return None


nums = [2, 7, 11, 15]
