from problems.day05 import Solution


def test_day05_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day05_examples():
    solution = Solution()

    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1


def test_day05_handles_zero_heights():
    solution = Solution()

    assert solution.maxArea([0, 0]) == 0


def test_day05_uses_farther_distance_when_helpful():
    solution = Solution()

    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
