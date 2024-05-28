from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1<<i for i in range(4)]
        mins = [1<<i for i in range(5)]

        al = [i<<i for i in range(9)]
        ans = []
        ans2 = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    ans.append(f"{i}:{j:02}")

        return ans