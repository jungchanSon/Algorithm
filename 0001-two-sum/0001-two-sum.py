class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            v = nums[i]
            v2 = target - v
            if v2 in nums[i+1:]:
                v2i = nums.index(v2,i+1)
                return [i, v2i ]