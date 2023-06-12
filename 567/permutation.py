class Solution:
    def permutation(self, dict):
        for i in dict:
            if dict[i] != 0:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = {}
        if len(s1)>len(s2):
            return False
        for i in s1:
            if i not in a:
                a[i] = 1
            else:
                a[i]+=1
        contador = 0
        for i in range(len(s1)):
            if s2[i] in a:
                contador+=1
                a[s2[i]]-=1
        if contador == len(s1) and self.permutation(a):
            return True
        else:
            for i in range (1,len(s2)-len(s1)+1):
                if contador == len(s1) and self.permutation(a):
                    return True
                if s2[i-1] in a:
                    contador-=1
                    a[s2[i-1]]+=1
                if s2[i+len(s1)-1] in a:
                    contador+=1
                    a[s2[i+len(s1)-1]]-=1
            if contador == len(s1) and self.permutation(a):
                return True
        return False
