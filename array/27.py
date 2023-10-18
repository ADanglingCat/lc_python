# 移除元素
class Solution(object):
    def removeElement(self, nums, val):
        slow = 0

        for fast in nums:
            if fast != val:
                nums[slow] = fast
                slow += 1
        return slow


s = Solution()
nums = [1, 2, 5, 6]
ret = s.removeElement(nums, 5)
print(nums)
print(ret)
