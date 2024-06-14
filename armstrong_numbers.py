class Solution:
    def armstrongNumber (self, n):
        s = 0
        
        for i in str(n):
            i = int(i)
            s += (i ** len(str(n)))
            
        return 'true' if s == n else 'false'
