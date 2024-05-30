class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)