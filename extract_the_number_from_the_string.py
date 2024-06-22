class Solution:
    def isNum(self, n):
        if n[0] >= '0' and n[0] <= '8' and '9' not in n:
            return int(n)
        else:
            return -1
            
    def ExtractNumber(self,sentence):
        return max(map(self.isNum, sentence.split()))
