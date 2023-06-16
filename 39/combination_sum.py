class Solution:
    def aux(self, candidates, target, suma, lista_solucion, temporal):
        if suma == target:
            organizado = sorted(temporal)
            if organizado not in lista_solucion:
                lista_solucion.append(organizado)
            return

        if suma > target:
            return

        for i in candidates:
            temporal.append(i)
            suma += i
            self.aux(candidates, target, suma, lista_solucion, temporal)
            suma -= i
            temporal.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lista_solucion = []
        temporal = []
        self.aux(candidates, target, 0, lista_solucion, temporal)
        return lista_solucion
