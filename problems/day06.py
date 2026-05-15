"""Day 06: DSA practice workspace."""


from typing import List


QUESTION = """
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Examples:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""


class Solution:
    """Trapping Rain Water solution."""

    def trap(self, height: List[int]) -> int:
        # Two pointers scan inward. At each step, the lower side controls
        # how much water can be trapped at that position.
        left = 0
        right = len(height) - 1

        # Best wall seen so far from each side.
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])

                # Water above this bar is limited by the best left wall,
                # because the right side is already taller.
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])

                # Water above this bar is limited by the best right wall,
                # because the left side is at least as tall.
                water += right_max - height[right]
                right -= 1

        return water


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]

    for height, expected in checks:
        assert solution.trap(height) == expected

    print("All Day 06 checks passed.")
