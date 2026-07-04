from problems.day22 import Solution


def test_day22_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day22_examples():
    solution = Solution()

    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


def test_day22_handles_single_element():
    solution = Solution()

    assert solution.runningSum([5]) == [5]


def test_day22_handles_negative_numbers():
    solution = Solution()

    assert solution.runningSum([-1, 2, -3, 4]) == [-1, 1, -2, 2]
