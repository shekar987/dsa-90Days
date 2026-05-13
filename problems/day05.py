"""Day 05: DSA practice workspace."""

from typing import List


QUESTION = """
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place so each unique element appears only once. Keep the
relative order of the elements the same.

Return k, the number of unique elements. The first k elements of nums should
contain the unique values in sorted order. Anything after index k - 1 can be
ignored.

Examples:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


class Solution:
    """Remove Duplicates from Sorted Array solution."""

    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([1], [1]),
    ]

    for nums, expected in checks:
        k = solution.removeDuplicates(nums)
        assert k == len(expected)
        assert nums[:k] == expected

    print("All Day 05 checks passed.")
