"""Day 22: DSA practice workspace."""


from typing import List


QUESTION = """
1480. Running Sum of 1d Array

Given an array nums, define a running sum of an array as:
runningSum[i] = sum(nums[0] ... nums[i]).

Return the running sum of nums.

Examples:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""


class Solution:
    """Running Sum of 1d Array solution."""

    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for num in nums:
            # Add the current number to everything seen before it.
            total += num

            # Store the sum from nums[0] through the current index.
            result.append(total)

        return result


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ]

    for nums, expected in checks:
        assert solution.runningSum(nums) == expected

    print("All Day 22 checks passed.")
