class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pr = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in pr:
                return [pr[diff], i]
            else:
                pr[j] = i
        