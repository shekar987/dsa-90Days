from problems.day19 import Solution


def test_day19_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day19_examples():
    solution = Solution()

    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False


def test_day19_handles_k_zero():
    solution = Solution()

    assert solution.containsNearbyDuplicate([1, 1], 0) is False


def test_day19_handles_duplicate_too_far_apart():
    solution = Solution()

    assert solution.containsNearbyDuplicate([1, 2, 1], 1) is False


def test_day19_handles_multiple_updates_to_same_value():
    solution = Solution()

    assert solution.containsNearbyDuplicate([1, 2, 1, 1], 1) is True
