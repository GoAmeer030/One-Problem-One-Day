class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        s = {i:0 for i in range(n)}
        
        for i in roads:
            s[i[0]] += 1
            s[i[1]] += 1
            
        s = dict(sorted(s.items(), key=lambda item: item[1]))
        
        j = 1
        for i in s.keys():
            s[i] = j
            j += 1
        
        res = 0
        for i in roads:
            res += s[i[0]]
            res += s[i[1]]
            
        return res
