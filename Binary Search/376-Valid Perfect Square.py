
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num
        while left <= right:
            mid = (left + right) >> 1
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

num = 4
ans = Solution().isPerfectSquare(num)
print(ans)