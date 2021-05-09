from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(0, len(nums)):
            if val != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def removeElement(self, nums: List[int], val: int) -> int:
        other, target = 0, len(nums) - 1
        while other <= target:
            if nums[other] == val:
                nums[other] = nums[target]
                target -= 1
            else:
                other += 1
        return other

nums = [3, 2]
val = 3
ans = Solution().removeElement(nums, val)
print(ans)