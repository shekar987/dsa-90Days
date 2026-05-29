from problems.day11 import Solution


def test_day11_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day11_examples():
    solution = Solution()

    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False


def test_day11_handles_duplicate_letters():
    solution = Solution()

    assert solution.checkInclusion("aabc", "eidcbaaooo") is True


def test_day11_handles_exact_match():
    solution = Solution()

    assert solution.checkInclusion("abc", "abc") is True


def test_day11_returns_false_when_s1_is_longer():
    solution = Solution()

    assert solution.checkInclusion("abcd", "abc") is False
