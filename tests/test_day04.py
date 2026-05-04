from problems.day04 import Solution


def test_day04_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day04_examples():
    solution = Solution()

    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1


def test_day04_handles_zero_heights():
    solution = Solution()

    assert solution.maxArea([0, 0]) == 0


def test_day04_moves_past_taller_middle_lines():
    solution = Solution()

    assert solution.maxArea([1, 2, 4, 3]) == 4
