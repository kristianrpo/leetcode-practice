class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        existe = {}
        nums.sort()
        for i in range(len(nums)):
            p1 = i+1
            p2 = len(nums)-1
            while p1<p2:
                valor = nums[i]+nums[p1]+nums[p2]
                if valor==0:
                    agregar = [nums[i],nums[p1],nums[p2]]
                    if str(agregar) not in existe:
                        existe[str(agregar)] = agregar
                    p1+=1
                    p2-=1
                if valor>0:
                    p2-=1
                if valor<0:
                    p1+=1
        return existe.values()
