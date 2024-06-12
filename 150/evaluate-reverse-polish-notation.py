class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pila = []
        actual = 0
        operador = set(["*","+","/","-"])
        for i in tokens:
            if i in operador:
                a = int(pila.pop())
                b = int(pila.pop())
                if i == "+":
                    pila.append(b+a)
                if i == "*":
                    pila.append(b*a)
                if i == "/":
                    pila.append(b/a)
                if i == "-":
                    pila.append(b-a)
            else:
                pila.append(int(i))
        print(pila)
        return int(pila[0])