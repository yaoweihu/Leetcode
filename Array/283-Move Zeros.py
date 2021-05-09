from typing import List


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        left = 0
        for right in range(0, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                right += 1
        return nums


nums = [2, 0, 1, 0, 3, 12]
ans = Solution().moveZeros(nums)
print(ans)