class Solution {
  public:
    int findCrossOver(vector<int>& arr, int low, int high, int x) {
        if (arr[high] <= x) return high;
        if (arr[low] > x) return low;

        int mid = (low + high) / 2;

        if (arr[mid] <= x && arr[mid + 1] > x) return mid;
        else if (arr[mid] < x) return findCrossOver(arr, mid + 1, high, x);
        return findCrossOver(arr, low, mid - 1, x);
    }

    vector<int> printKClosest(vector<int>& arr, int n, int k, int x) {
        int crossoverIndex = findCrossOver(arr, 0, n - 1, x);
        int leftIndex = crossoverIndex;
        int rightIndex = crossoverIndex + 1;

        if (leftIndex >= 0 && arr[leftIndex] == x) leftIndex--;

        vector<int> closestElements;
        for (int i = 0; i < k; i++) {
            if (leftIndex >= 0 && rightIndex < n) {
                int leftDiff = x - arr[leftIndex];
                int rightDiff = arr[rightIndex] - x;
                if (leftDiff < rightDiff) {
                    closestElements.push_back(arr[leftIndex]);
                    leftIndex--;
                } else {
                    closestElements.push_back(arr[rightIndex]);
                    rightIndex++;
                }
            } else if (leftIndex >= 0) {
                closestElements.push_back(arr[leftIndex]);
                leftIndex--;
            } else {
                closestElements.push_back(arr[rightIndex]);
                rightIndex++;
            }
        }
        return closestElements;
    }
};