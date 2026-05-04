from problems.day02 import Solution


def test_day02_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day02_examples():
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_day02_handles_negative_numbers():
    solution = Solution()

    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
