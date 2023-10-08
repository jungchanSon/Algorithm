def solution(wallpaper):
    answer = 0
    l, r, t, b = -1, -1, -1, -1
    n, m = len(wallpaper), len(wallpaper[0])
    for i in range(n):
        if t == -1 and "#" in wallpaper[i]:
            t = i
            
        if '#' in wallpaper[i]:
            b = i+1
    
    for i in range(m):
        for j in range(n):
            if l == -1 and wallpaper[j][i] == "#":
                l = i

            if wallpaper[j][i] == "#":
                r = i+1

    return [t, l, b, r]