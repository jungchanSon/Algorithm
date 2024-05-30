class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_len = len(min(strs, key = lambda x: len(x)))
        if len(strs) == 0:
            return ""
        for i in range(min_len):
            cur = strs[0][i]
            flag = False
            for j in strs:
                if j[i] != cur:
                    flag = True
                    break
            if flag:
                break
            answer += strs[0][i]
        return answer