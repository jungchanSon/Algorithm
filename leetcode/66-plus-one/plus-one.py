class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dummy = "".join(map(str, digits))
        ans = list(str(int(dummy) + 1))
        return list(map(int, ans))