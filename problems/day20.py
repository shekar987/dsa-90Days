"""Day 20: DSA practice workspace."""


from typing import List


QUESTION = """
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Examples:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4].

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    """Longest Consecutive Sequence solution using a set."""

    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            # Only start counting from the beginning of a sequence.
            # If num - 1 exists, this number is in the middle of a sequence.
            if num - 1 not in numbers:
                current = num
                streak = 1

                # Count upward while the next consecutive number exists.
                while current + 1 in numbers:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
    ]

    for nums, expected in checks:
        assert solution.longestConsecutive(nums) == expected

    print("All Day 20 checks passed.")
