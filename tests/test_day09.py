from problems.day09 import Solution


def test_day09_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day09_examples():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3


def test_day09_handles_empty_string():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("") == 0


def test_day09_handles_spaces_and_symbols():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("a b!a") == 4


def test_day09_handles_repeated_character_after_window_start():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abba") == 2
