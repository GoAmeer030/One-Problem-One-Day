class Solution:
    def oddEven(self, s : str) -> str:
        lis = 'abcdefghijklmnopqrstuvwxyz'
        res = 0
        
        for i in set(s):
            if s.count(i) % 2 == (lis.index(i) + 1) % 2:
                res += 1
                
        return "EVEN" if res % 2 == 0 else "ODD"