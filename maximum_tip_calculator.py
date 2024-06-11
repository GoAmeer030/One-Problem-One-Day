class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        orders = sorted(range(n), key=lambda i: abs(arr[i] - brr[i]), reverse=True)
        total_tip = 0
        for i in orders:
            if (arr[i] >= brr[i] and x > 0) or y == 0:
                total_tip += arr[i]
                x -= 1
            else:
                total_tip += brr[i]
                y -= 1
        return total_tip
