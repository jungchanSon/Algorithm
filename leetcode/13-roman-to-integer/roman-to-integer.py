class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        symbol = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        value = (1, 5, 10, 50, 100, 500, 1000)
        symbol_value = dict()
        
        for i, v in enumerate(symbol):
            symbol_value[v] = value[i]
        
       
        prev = ""
        for i in s:
            if prev == "C" and (i == "D" or i == "M"):
                answer -= 2*symbol_value[prev]
            if prev == "X" and (i == "L" or i == "C"):
                answer -= 2*symbol_value[prev]
            if prev == "I" and (i == "V" or i == "X"):
                answer -= 2*symbol_value[prev]

            answer += symbol_value[i]
            prev = i
        
        return answer