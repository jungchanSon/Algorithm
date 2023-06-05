S = input().rstrip().upper()
range_AtoZ = ord('Z') - ord('A')
ord_A = ord('A')
ans = ""

for i in range(range_AtoZ+1):
    result = S.find(chr(ord_A+i))
    ans += str(result) + " "
print(ans)