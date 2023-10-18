# 双指针
class Solution(object):
    def sortedSquare(self, nums):
        length = len(nums)
        ret = [0 for _ in range(length)]
        left, right, index = 0, length - 1, length - 1
        while left <= right:
            print(index)
            if nums[left] * nums[left] > nums[right] * nums[right]:
                ret[index] = nums[left] * nums[left]
                left += 1
            else:
                ret[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return ret


solution = Solution()
aret = solution.sortedSquare([-4, -1, 0, 3, 10])

