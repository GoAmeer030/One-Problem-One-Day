class Solution:
    def numberOfConsecutiveOnes (ob,n):
        mod=10**9+7
        p,q,r=0,1,1
        for i in range(3,n+1):
            a=(p+q)%mod
            r=(2*r+a)%mod
            p=q
            q=a
        return r