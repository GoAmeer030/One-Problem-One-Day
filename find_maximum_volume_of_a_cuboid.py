class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        l = (perimeter - math.sqrt(perimeter * perimeter - 24 * area)) / 12
        h=(perimeter/4)-(2*l)
        V=l*l*h
        return V
