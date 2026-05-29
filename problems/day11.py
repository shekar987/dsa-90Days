"""Day 11: DSA practice workspace."""


QUESTION = """
567. Permutation in String

Given two strings s1 and s2, return True if s2 contains a permutation of s1,
or False otherwise.

In other words, return True if one of s1's permutations is a substring of s2.

Examples:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True

Input: s1 = "ab", s2 = "eidboaoo"
Output: False

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    """Permutation in String solution."""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        window_size = len(s1)

        # Build counts for s1 and for the first window in s2.
        for index in range(window_size):
            s1_count[ord(s1[index]) - ord("a")] += 1
            window_count[ord(s2[index]) - ord("a")] += 1

        if s1_count == window_count:
            return True

        # Slide a fixed-size window across s2.
        for right in range(window_size, len(s2)):
            left = right - window_size

            # Add the new right character and remove the old left character.
            window_count[ord(s2[right]) - ord("a")] += 1
            window_count[ord(s2[left]) - ord("a")] -= 1

            if s1_count == window_count:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
    ]

    for s1, s2, expected in checks:
        assert solution.checkInclusion(s1, s2) is expected

    print("All Day 11 checks passed.")
