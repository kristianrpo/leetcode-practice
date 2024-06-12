class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        puntero_inicial = 0
        puntero_final = len(numbers)-1
        while(puntero_inicial<puntero_final):
            valor = numbers[puntero_inicial] + numbers[puntero_final]
            if valor == target:
                return [puntero_inicial+1,puntero_final+1]
            if valor > target:
                puntero_final-=1
            if valor<target:
                puntero_inicial+=1