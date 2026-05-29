"""Day 10: DSA practice workspace."""


QUESTION = """
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Examples:
Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    """Longest Repeating Character Replacement solution."""

    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        most_frequent = 0
        longest = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1

            # Most common letter in the current window. Everything else
            # would need to be replaced to make the window one repeated char.
            most_frequent = max(most_frequent, counts[char])

            window_length = right - left + 1

            # If replacements needed are more than k, the window is invalid.
            if window_length - most_frequent > k:
                counts[s[left]] -= 1
                left += 1
                window_length -= 1

            longest = max(longest, window_length)

        return longest


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 0, 4),
    ]

    for text, replacements, expected in checks:
        assert solution.characterReplacement(text, replacements) == expected

    print("All Day 10 checks passed.")
