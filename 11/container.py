class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        maximus = -1
        while p1<p2:
            base = p2-p1
            min_height = min(height[p1],height[p2])
            if maximus < base*min_height:
                maximus = base*min_height
            if height[p1] == height[p2]:
                p1+=1
                p2-=1
                continue
            if height[p1] == min_height:
                p1+=1
            if height[p2] == min_height:
                p2-=1
        return maximus
