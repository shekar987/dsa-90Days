"""Day 23: DSA practice workspace."""


from typing import List


QUESTION = """
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    """Subarray Sum Equals K solution using prefix sums."""

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        total = 0

        for num in nums:
            current_sum += num

            # If current_sum - k appeared before, every such earlier prefix
            # creates a subarray ending here with sum k.
            needed_prefix = current_sum - k
            total += prefix_count.get(needed_prefix, 0)

            # Save this prefix sum for future subarrays.
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return total


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
    ]

    for nums, k, expected in checks:
        assert solution.subarraySum(nums, k) == expected

    print("All Day 23 checks passed.")
