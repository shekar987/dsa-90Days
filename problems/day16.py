"""Day 16: DSA practice workspace."""


QUESTION = """
242. Valid Anagram

Given two strings s and t, return True if t is an anagram of s, and False
otherwise.

Examples:
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow-up:
If the inputs contain Unicode characters, a hash map still works because it
can count any character key, not just lowercase English letters.
"""


class Solution:
    """Valid Anagram solution using hash maps."""

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for index in range(len(s)):
            # Count each character in both strings at the same position.
            s_count[s[index]] = s_count.get(s[index], 0) + 1
            t_count[t[index]] = t_count.get(t[index], 0) + 1

        # Same character counts means one string can be rearranged into the other.
        return s_count == t_count


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
    ]

    for s, t, expected in checks:
        assert solution.isAnagram(s, t) is expected

    print("All Day 16 checks passed.")
