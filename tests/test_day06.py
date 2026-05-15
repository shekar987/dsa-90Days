from problems.day06 import Solution


def test_day06_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day06_examples():
    solution = Solution()

    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([4, 2, 0, 3, 2, 5]) == 9


def test_day06_handles_no_trapped_water():
    solution = Solution()

    assert solution.trap([1, 2, 3, 4]) == 0
    assert solution.trap([4, 3, 2, 1]) == 0


def test_day06_handles_small_inputs():
    solution = Solution()

    assert solution.trap([0]) == 0
    assert solution.trap([2, 0, 2]) == 2
