class Solution:
    def maxVowels(SELF,s: str, k: int) -> int:
        vowels = set(["a","e","i","o","u"])
        count = 0
        maxx = -1000
        for i in range(k):
            if s[i] in vowels:
                count+=1
        if count>maxx:
            maxx = count
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                count-=1
            if s[i+k-1] in vowels:
                count+=1
            if count>maxx:
                maxx = count
        return maxx
# Concepto de ventanas      
