data = int(input())
if data%4 == 0:
    if data%100 or data % 400==0:
            print(1)
            quit()
            
print(0)