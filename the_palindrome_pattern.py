class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
        
    def pattern (self, arr):
        l = len(arr)
        for i in range(l):
            if self.isPalindrome(arr[i]):
                return str(i) + " R" 
                
        j = 0
        while j<l :
            s = ""
            for i in arr:
                s += str(i[j])
            
            if(self.isPalindrome(s)):
                return str(j) + " C"
            
            j += 1
            
        return -1
