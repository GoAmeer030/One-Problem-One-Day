class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        i = 0
        while i < n-1 and arr[i] > k:
            i += 1
        r = arr[i] if arr[i] <= k else 0
        j = i + 1
        temp = r
        while i < j and j < n:
            if arr[j] <= k:
                temp += arr[j]
                j += 1
            else:
                i = j
                while i < n-1 and arr[i] > k:
                    i += 1
                j = i + 1
                temp = arr[i] if arr[i] <= k else 0
            r = max(temp, r)
        return r