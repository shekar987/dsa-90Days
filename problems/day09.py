"""Day 09: DSA practice workspace."""


QUESTION = """
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate
characters.

Examples:
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    """Longest Substring Without Repeating Characters solution."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        window = set()

        for right, char in enumerate(s):
            # If char is already in the current window, move left forward
            # until that duplicate is removed.
            while char in window:
                window.remove(s[left])
                left += 1

            # Now s[left:right + 1] has no repeated characters.
            window.add(char)
            current_length = right - left + 1
            longest = max(longest, current_length)

        return longest


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]

    for text, expected in checks:
        assert solution.lengthOfLongestSubstring(text) == expected

    print("All Day 09 checks passed.")
