import turtle as t
import random

t.shape("turtle")
t.speed(0)
t.penup()
def draw_rect(x, y, value, thin):
    if type(value) == int:
        t.color("black")
        t.setposition(x, y)
        t.pendown()

        t.begin_fill()
        t.setposition(x, y+value)
        t.setposition(x+thin, y+value)
        t.setposition(x+thin, y)

        t.end_fill()
        t.penup()
    
    else :
        t.color("green")
        t.setposition(x, y)
        t.pendown()

        t.begin_fill()
        t.setposition(x, y+value[0])
        t.setposition(x+thin, y+value[0])
        t.setposition(x+thin, y)

        t.end_fill()
        t.penup()
# draw_rect(-100, 0, 0)
# draw_rect(-99, 0, 100)
# draw_rect(-97, 0, 300)

"""
    create_arrays(n: 개수, r: 범위)
    1 ~ r의 랜덤값을 추출.
"""
def create_arrays(n, r): 
    arr = []
    for _ in range(n):
        arr.append(random.randrange(1, r))
    
    return arr

def draw_canvas(arr, thin):
    start_x = -200
    for i in range(len(arr)):
        draw_rect(start_x + i * thin, 0, arr[i], thin)


def selection_sort(arr):
    l = len(arr)
    draw_canvas(arr, 5)
    for i in range(l):
        t.speed(0)
        t.penup()
        current = i
        for j in range(i, l):
            if arr[j] < arr[current]:
                current = j
        temp = arr[i]
        arr[i] = (arr[current], 1)
        arr[current] = (temp, 2)
        
        draw_canvas(arr, 5)
        
        
# rand_arr = create_arrays(30, 300)
# selection_sort(rand_arr)

