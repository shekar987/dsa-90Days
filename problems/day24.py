"""Day 24: DSA practice workspace."""

from typing import List


QUESTION = """
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:
calculate the sum of the elements of nums between indices left and right
inclusive, where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) initializes the object with the integer array nums.
- int sumRange(int left, int right) returns the sum of nums[left..right].

Example:
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2,0,3,-5,2,-1]], [0,2], [2,5], [0,5]]

Output:
[null, 1, -1, -3]
"""


class NumArray:
    """Range Sum Query solution using prefix sums."""

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0]

        for num in nums:
            # prefix_sums[i] stores the sum of the first i numbers.
            self.prefix_sums.append(self.prefix_sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right is:
        # sum(nums[0:right + 1]) - sum(nums[0:left])
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


if __name__ == "__main__":
    nums = NumArray([-2, 0, 3, -5, 2, -1])

    assert nums.sumRange(0, 2) == 1
    assert nums.sumRange(2, 5) == -1
    assert nums.sumRange(0, 5) == -3

    print("All Day 24 checks passed.")
