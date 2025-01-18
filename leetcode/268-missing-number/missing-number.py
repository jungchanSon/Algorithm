class Solution(object):
    def missingNumber(self, nums):
        setList = set([i for i in range(len(nums)+1)])
        nums = set(nums)
        result = list(set.difference(setList, nums))
        if len(result) == 0:
            return 
        else :
            return result.pop()
"""
        :type nums: List[int]
        :rtype: int
"""
    