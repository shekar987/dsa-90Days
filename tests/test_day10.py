from problems.day10 import Solution


def test_day10_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day10_examples():
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4


def test_day10_handles_no_replacements():
    solution = Solution()

    assert solution.characterReplacement("AABB", 0) == 2


def test_day10_handles_all_same_characters():
    solution = Solution()

    assert solution.characterReplacement("AAAA", 0) == 4


def test_day10_handles_large_replacement_budget():
    solution = Solution()

    assert solution.characterReplacement("ABCDE", 4) == 5
