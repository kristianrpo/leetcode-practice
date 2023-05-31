class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diccionario = {}
        lista = []
        for element in nums:
            if element not in diccionario:
                diccionario[element] = 0
            else:
                diccionario[element] = diccionario[element]+1
        for i in range (k):
            max_value = max(diccionario, key=diccionario.get)
            lista.append(max_value)
            diccionario.pop(max_value)
        return lista
