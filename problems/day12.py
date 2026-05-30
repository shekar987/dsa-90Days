"""Day 12: DSA practice workspace."""


QUESTION = """
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t, including duplicates,
is included in the window. If there is no such substring, return "".

The test cases are generated so the answer is unique.

Examples:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    """Minimum Window Substring solution."""

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        have = 0
        required = len(need)
        left = 0
        best_start = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            # A required character is satisfied only when its count matches
            # exactly what t needs.
            if char in need and window[char] == need[char]:
                have += 1

            # Once the window contains all required characters, shrink it
            # from the left to find the smallest valid version.
            while have == required:
                current_length = right - left + 1
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                left_char = s[left]
                window[left_char] -= 1

                # If removing left_char makes the window miss a required
                # count, the window is no longer valid.
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]

    for s, t, expected in checks:
        assert solution.minWindow(s, t) == expected

    print("All Day 12 checks passed.")
