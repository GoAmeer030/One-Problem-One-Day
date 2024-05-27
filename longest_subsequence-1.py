from typing import List
from collections import defaultdict


class Solution:
    def longestSubseq(self, n : int, arr : List[int]) -> int:
        hmap = defaultdict(int)
        ans = float("-inf")
        for i in range(n):
            hmap[arr[i]] = max(hmap[arr[i]-1], hmap[arr[i] + 1]) + 1
            ans = max(ans, hmap[arr[i]])
        return ans