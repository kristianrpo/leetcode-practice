class Solution:
    def isValid(self, s: str) -> bool:
        elements = []
        diccionario = {")":"(","]":"[","}":"{"}
        for caracter in s:
            if caracter == "(" or caracter == "[" or caracter == "{":
                elements.append(caracter)
            if caracter == ")" or caracter == "]" or caracter == "}":
                if diccionario[caracter] not in elements:
                    return False
                if elements[len(elements)-1] == diccionario[caracter]:
                    elements.pop(len(elements)-1)
                else:
                    return False
        if len(elements)>0:
            return False
        else:
            return True
