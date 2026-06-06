from problems.day13 import Solution


def test_day13_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day13_examples():
    solution = Solution()

    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23


def test_day13_handles_all_negative_numbers():
    solution = Solution()

    assert solution.maxSubArray([-3, -2, -5]) == -2


def test_day13_handles_zero_and_negative_numbers():
    solution = Solution()

    assert solution.maxSubArray([-2, 0, -1]) == 0


def test_day13_handles_best_subarray_at_end():
    solution = Solution()

    assert solution.maxSubArray([-1, -2, 3, 4]) == 7
