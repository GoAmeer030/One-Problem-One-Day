class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        x=k%len(mat[0])
        if x==0:
            return mat
        for i in range(len(mat)):
            mat[i]=mat[i][x:]+mat[i][:x]
        return mat
