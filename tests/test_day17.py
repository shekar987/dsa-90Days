from problems.day17 import Solution


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


def test_day17_solution_can_be_created():
    solution = Solution()

    assert isinstance(solution, Solution)


def test_day17_examples():
    solution = Solution()

    assert normalize(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == normalize(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert solution.groupAnagrams([""]) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]


def test_day17_groups_words_with_repeated_letters():
    solution = Solution()

    assert normalize(solution.groupAnagrams(["abb", "bab", "bba", "abc"])) == normalize(
        [["abb", "bab", "bba"], ["abc"]]
    )


def test_day17_keeps_non_anagrams_separate():
    solution = Solution()

    assert normalize(solution.groupAnagrams(["a", "b", "c"])) == normalize([["a"], ["b"], ["c"]])
