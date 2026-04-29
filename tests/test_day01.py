from problems.day01 import Solution


def test_day01_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day01_examples():
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True


def test_day01_handles_numbers_and_symbols():
    solution = Solution()

    assert solution.isPalindrome("0P") is False
    assert solution.isPalindrome("No 'x' in Nixon") is True
