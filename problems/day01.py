"""Day 01: DSA practice workspace."""


class Solution:
    """Valid Palindrome solution."""

    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]

    for text, expected in checks:
        assert solution.isPalindrome(text) is expected

    print("All Day 01 checks passed.")
