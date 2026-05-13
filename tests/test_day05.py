from problems.day05 import Solution


def assert_remove_duplicates(nums: list[int], expected: list[int]) -> None:
    solution = Solution()

    k = solution.removeDuplicates(nums)

    assert k == len(expected)
    assert nums[:k] == expected


def test_day05_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day05_examples():
    assert_remove_duplicates([1, 1, 2], [1, 2])
    assert_remove_duplicates(
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [0, 1, 2, 3, 4],
    )


def test_day05_handles_single_value():
    assert_remove_duplicates([1], [1])


def test_day05_handles_all_duplicates():
    assert_remove_duplicates([2, 2, 2], [2])


def test_day05_handles_no_duplicates():
    assert_remove_duplicates([-2, -1, 0, 1], [-2, -1, 0, 1])
