"""Day 05: DSA practice workspace."""


from typing import List


QUESTION = """
11. Container With Most Water

Given an integer array height of length n, there are n vertical lines where
the endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container that stores
the most water. Return the maximum amount of water the container can store.
You may not slant the container.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


class Solution:
    """Container With Most Water solution."""

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = width * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ]

    for height, expected in checks:
        assert solution.maxArea(height) == expected

    print("All Day 05 checks passed.")
