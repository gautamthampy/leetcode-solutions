from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force -> use nested loops and check for each possible pair that adds up to the target -> o(n^2)
        # two pointer -> the list has to be sorted, python uses timsort inbuilt which has sc of o(n), so better to use hashmap
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            else:
                map[num] = i

sol = Solution()
nums = [2, 7, 11, 15]
target = 9
res = sol.twoSum(nums, target)
print(res)                 