class Solution:
    def findExtra(self,n,a,b):
        i , j = 0, n-1
        while(i <= j and i < n and j > 0):
            if a[i] != b[i]:
                return i
            if a[j] != b[j-1]:
                return j
                
            i += 1
            j -= 1
        return i
