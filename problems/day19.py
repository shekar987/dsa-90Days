"""Day 19: DSA practice workspace."""


from typing import List


QUESTION = """
219. Contains Duplicate II

Given an integer array nums and an integer k, return True if there are two
distinct indices i and j in the array such that nums[i] == nums[j] and
abs(i - j) <= k.

Examples:
Input: nums = [1,2,3,1], k = 3
Output: True

Input: nums = [1,0,1,1], k = 1
Output: True

Input: nums = [1,2,3,1,2,3], k = 2
Output: False
"""


class Solution:
    """Contains Duplicate II solution using a hash map."""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for index, num in enumerate(nums):
            # If we saw the same number before, check whether the old index
            # is close enough to the current index.
            if num in last_seen and index - last_seen[num] <= k:
                return True

            # Store the latest index. The newest index is always best for
            # future distance checks because it is closest to later elements.
            last_seen[num] = index

        return False


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]

    for nums, k, expected in checks:
        assert solution.containsNearbyDuplicate(nums, k) is expected

    print("All Day 19 checks passed.")
