"""Day 02: DSA practice workspace."""


from typing import List


class Solution:
    """Two Sum solution."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

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

    print("All Day 02 checks passed.")
