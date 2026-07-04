from problems.day20 import Solution


def test_day20_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day20_examples():
    solution = Solution()

    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_day20_handles_empty_input():
    solution = Solution()

    assert solution.longestConsecutive([]) == 0


def test_day20_handles_duplicates():
    solution = Solution()

    assert solution.longestConsecutive([1, 2, 2, 3]) == 3


def test_day20_handles_negative_numbers():
    solution = Solution()

    assert solution.longestConsecutive([-3, -2, -1, 5]) == 3


def test_day20_handles_single_value():
    solution = Solution()

    assert solution.longestConsecutive([7]) == 1
