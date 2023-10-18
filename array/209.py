# 滑动窗口
class Solution:
    def midSubArrayLen(self, target, nums):
        ret = float("inf")
        i = 0
        tempSum = 0
        for j in range(len(nums)):
            tempSum += nums[j]
            while tempSum >= target:
                ret = min(ret, j - i + 1)
                tempSum -= nums[i]
                i += 1
        return 0 if ret == float("inf") else ret




