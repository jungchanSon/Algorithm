def solution(s:str):
    answer = 0
    
    l = ["zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"]

    for i in range(10):
        s= s.replace(l[i], str(i) )
    
    return int(s) 

