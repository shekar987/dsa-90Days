from problems.day18 import Solution


def test_day18_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day18_examples():
    solution = Solution()

    assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert solution.topKFrequent([1], 1) == [1]


def test_day18_handles_negative_numbers():
    solution = Solution()

    assert set(solution.topKFrequent([-1, -1, -2, -2, -2, 3], 2)) == {-1, -2}


def test_day18_handles_k_equal_unique_count():
    solution = Solution()

    assert set(solution.topKFrequent([4, 4, 6, 6, 7], 3)) == {4, 6, 7}


def test_day18_handles_single_top_value():
    solution = Solution()

    assert solution.topKFrequent([5, 5, 5, 1, 1, 2], 1) == [5]
