class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1]*n
        maximum = -1

        for i in range(n-1, -1, -1):
            ans[i] = maximum
            maximum = max(maximum, arr[i])

        return ans