"""Day 13: DSA practice workspace."""


from typing import List


QUESTION = """
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray with the largest
sum and return that sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


class Solution:
    """Maximum Subarray solution."""

    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        best_sum = nums[0]

        for num in nums[1:]:
            # Either extend the previous subarray or start a new one here.
            current_sum = max(num, current_sum + num)

            # Track the best subarray sum seen anywhere so far.
            best_sum = max(best_sum, current_sum)

        return best_sum


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]

    for nums, expected in checks:
        assert solution.maxSubArray(nums) == expected

    print("All Day 13 checks passed.")
