while 1:
    data = input().rstrip()
    if data == "0":
        break
    
    data = list(data)
    if data == list(reversed(data)):
        print("yes")
    else:
        print("no")