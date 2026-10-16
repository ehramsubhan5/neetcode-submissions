class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest = 0

        while l < r:
            heightLower = min(heights[l], heights[r])
            container = heightLower * (r - l)
            largest = max(largest, container)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return largest