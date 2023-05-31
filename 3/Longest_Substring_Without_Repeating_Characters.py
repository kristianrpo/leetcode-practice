class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>0:
            values = []
            for i in range(len(s)):
                count_without = 1
                list_repetead = []
                list_repetead.append(s[i])
                for j in range(i, len(s)):
                    if s[j] not in list_repetead:
                        list_repetead.append(s[j])
                        count_without+=1
                    else:
                        if i==j:
                            continue
                        else:
                            values.append(count_without)
                            break
                values.append(count_without)
            return max(values)
        else:
            return 0
