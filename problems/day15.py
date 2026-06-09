"""Day 15: DSA practice workspace."""


from typing import List


QUESTION = """
1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume each input has exactly one solution, and you may not use the
same element twice. You can return the answer in any order.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    """Two Sum hash map solution."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            # If complement was seen earlier, that earlier index and the
            # current index form the required pair.
            if complement in seen:
                return [seen[complement], index]

            # Save the current number for future numbers to match against.
            seen[num] = index

        raise ValueError("No valid two sum solution found.")


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in checks:
        assert solution.twoSum(nums, target) == expected

    print("All Day 15 checks passed.")
