class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        max_l = height[p1]
        max_r = height[p2]
        acumulador = 0
        while(p1<p2):
            if height[p1]<=height[p2]:
                p1+=1
                max_l = max(max_l, height[p1])
                acumulador = acumulador + max_l-height[p1]
            else:
                p2-=1
                max_r = max(max_r, height[p2])
                acumulador = acumulador + max_r-height[p2]
        return acumulador
