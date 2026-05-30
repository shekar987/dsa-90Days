from problems.day12 import Solution


def test_day12_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day12_examples():
    solution = Solution()

    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""


def test_day12_handles_duplicate_required_characters():
    solution = Solution()

    assert solution.minWindow("AAABBC", "AABC") == "AABBC"


def test_day12_handles_no_valid_window():
    solution = Solution()

    assert solution.minWindow("abc", "d") == ""


def test_day12_is_case_sensitive():
    solution = Solution()

    assert solution.minWindow("aAaBb", "AB") == "AaB"
