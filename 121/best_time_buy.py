class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimo = 100000000
        ganancia = 0
        for precio in prices:
            if precio<=minimo:
                minimo = precio
            else:
                if precio-minimo >= ganancia:
                    ganancia = precio - minimo
        return ganancia
