from problems.day16 import Solution


def test_day16_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day16_examples():
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False


def test_day16_returns_false_for_different_lengths():
    solution = Solution()

    assert solution.isAnagram("ab", "a") is False


def test_day16_handles_repeated_letters():
    solution = Solution()

    assert solution.isAnagram("aabb", "baba") is True


def test_day16_handles_same_length_not_anagram():
    solution = Solution()

    assert solution.isAnagram("aacc", "ccac") is False
