from collections import defaultdict
from typing import List


class Solution:
    # Đề bài yêu cầu group vào 1 list ans strs hợp lệ (anagram)
    # Ý tưởng: Sorted word sau đó append word sorted vào 1 HashMap
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())
    # Time Complexity: O(N * NlogN) -> N * logN for sorted function
    # Space Complexity: O(N)
