from problems.day25 import Solution


def test_day25_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day25_examples():
    solution = Solution()

    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0


def test_day25_returns_leftmost_pivot():
    solution = Solution()

    assert solution.pivotIndex([0, 0, 0]) == 0


def test_day25_handles_pivot_at_end():
    solution = Solution()

    assert solution.pivotIndex([-1, 1, 0]) == 2


def test_day25_handles_negative_numbers():
    solution = Solution()

    assert solution.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2
