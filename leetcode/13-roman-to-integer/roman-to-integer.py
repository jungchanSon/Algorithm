class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        symbol = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        value = (1, 5, 10, 50, 100, 500, 1000)
        symbol_value = dict()
        
        for i, v in enumerate(symbol):
            symbol_value[v] = value[i]
        
        prev = ""
        special = ("I", "X", "C")
        special_dict = dict()
        special_dict["I"] = ("V", "X")
        special_dict["X"] = ("L", "C")
        special_dict["C"] = ("D", "M")

        for i in s:
            if prev in special and i in special_dict[prev] :
                answer -= 2*symbol_value[prev]
            answer += symbol_value[i]
            prev = i
        
        return answer