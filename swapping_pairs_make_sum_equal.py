class Solution:
    def findSwapValues(self, a, n, b, m):
        # Your code goes here
        a.sort()
        b.sort()
        a_sum = sum(a)
        b_sum = sum(b)
        if ((a_sum - b_sum) % 2) != 0:
            return -1

        target = (a_sum - b_sum) // 2

        # We are using set to provide the efficient average-case lookup time

        a = set(a)
        for i in b:
            if target + i in a:
                return 1
        return -1
