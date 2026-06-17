"""Day 17: DSA practice workspace."""


from typing import List


QUESTION = """
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

Examples:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    """Group Anagrams solution using a hash map."""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            # Convert each word into a frequency signature.
            # Anagrams have the same signature, such as eat/tea/ate.
            for char in word:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            # Put words with the same signature into the same bucket.
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    def normalize(groups: List[List[str]]) -> List[List[str]]:
        return sorted(sorted(group) for group in groups)

    solution = Solution()
    checks = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for words, expected in checks:
        assert normalize(solution.groupAnagrams(words)) == normalize(expected)

    print("All Day 17 checks passed.")
