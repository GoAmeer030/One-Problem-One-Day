class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        res = [0]
        xor_val = 0
        for op, val in queries:
            if op == 0:
                res.append(val ^ xor_val)
            else:
                xor_val ^= val
        res = [val ^ xor_val for val in res]
        res.sort()
        return res
