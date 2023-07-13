class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            remain = target - nums[i]
            nums[i] = None
            if remain in nums:
                return [i, nums.index(remain)]