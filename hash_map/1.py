class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records = dict()
        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]
            records[value] = index
        return []