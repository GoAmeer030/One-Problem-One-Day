class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        for a in range(2, n // 2 + 1):
            b = n - a
            if self.is_prime(a) and self.is_prime(b):
                return [a, b]
        return [-1, -1]
    def is_prime(self, num):
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True