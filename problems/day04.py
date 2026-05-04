"""Day 04: DSA practice workspace."""


from typing import List


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

    print("All Day 04 checks passed.")
