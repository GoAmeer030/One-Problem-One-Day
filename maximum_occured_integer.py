class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        arr = [0] * (maxx + 2)
        
        for i in range(n):
            arr[l[i]] += 1
            arr[r[i] + 1] -= 1
        
        max_count = arr[0]
        max_element = 0
        for i in range(1, maxx + 1):
            arr[i] += arr[i - 1]
            if max_count < arr[i]:
                max_count = arr[i]
                max_element = i
        
        return max_element
