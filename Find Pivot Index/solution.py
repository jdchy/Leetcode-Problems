class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for index, val in enumerate(nums):
            r -= val
            if l == r:
                return index
            l += val
        return -1