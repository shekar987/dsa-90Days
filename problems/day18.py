"""Day 18: DSA practice workspace."""


from typing import List


QUESTION = """
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, number of unique elements in nums]
"""


class Solution:
    """Top K Frequent Elements solution using bucket sort."""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # buckets[frequency] stores all numbers that appear exactly frequency times.
        # The maximum possible frequency is len(nums), so we create len(nums) + 1 buckets.
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in counts.items():
            buckets[frequency].append(num)

        result = []

        # Walk from high frequency to low frequency until we collect k numbers.
        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
    ]

    for nums, k, expected in checks:
        assert set(solution.topKFrequent(nums, k)) == expected

    print("All Day 18 checks passed.")
