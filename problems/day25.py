"""Day 25: DSA practice workspace."""


from typing import List


QUESTION = """
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all numbers strictly to the
left of the index is equal to the sum of all numbers strictly to the right.

If the index is on the left edge, the left sum is 0. If the index is on the
right edge, the right sum is 0.

Return the leftmost pivot index. If no such index exists, return -1.

Examples:
Input: nums = [1,7,3,6,5,6]
Output: 3

Input: nums = [1,2,3]
Output: -1

Input: nums = [2,1,-1]
Output: 0
"""


class Solution:
    """Find Pivot Index solution using prefix sums."""

    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for index, num in enumerate(nums):
            # Right sum is everything except the left side and current number.
            right_sum = total_sum - left_sum - num

            # The first balanced index is the leftmost pivot.
            if left_sum == right_sum:
                return index

            # Move current number into the left side for the next index.
            left_sum += num

        return -1


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
    ]

    for nums, expected in checks:
        assert solution.pivotIndex(nums) == expected

    print("All Day 25 checks passed.")
