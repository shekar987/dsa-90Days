from problems.day03 import Solution


def normalize(triplets: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(triplet) for triplet in triplets)


def test_day03_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day03_examples():
    solution = Solution()

    assert normalize(solution.threeSum([-1, 0, 1, 2, -1, -4])) == normalize(
        [[-1, -1, 2], [-1, 0, 1]]
    )
    assert solution.threeSum([0, 1, 1]) == []
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]


def test_day03_skips_duplicate_triplets():
    solution = Solution()

    assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_day03_handles_mixed_values():
    solution = Solution()

    assert normalize(solution.threeSum([-2, 0, 1, 1, 2])) == normalize(
        [[-2, 0, 2], [-2, 1, 1]]
    )
