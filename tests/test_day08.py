from problems.day08 import Solution


def test_day08_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day08_examples():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0


def test_day08_handles_single_day():
    solution = Solution()

    assert solution.maxProfit([5]) == 0


def test_day08_handles_flat_prices():
    solution = Solution()

    assert solution.maxProfit([3, 3, 3]) == 0


def test_day08_handles_best_sale_at_end():
    solution = Solution()

    assert solution.maxProfit([2, 1, 2, 0, 1]) == 1
