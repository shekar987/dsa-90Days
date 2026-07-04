from problems.day23 import Solution


def test_day23_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day23_examples():
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2


def test_day23_handles_negative_numbers():
    solution = Solution()

    assert solution.subarraySum([1, -1, 0], 0) == 3


def test_day23_handles_no_matching_subarray():
    solution = Solution()

    assert solution.subarraySum([1, 2, 3], 7) == 0


def test_day23_handles_repeated_prefix_sums():
    solution = Solution()

    assert solution.subarraySum([0, 0, 0], 0) == 6
