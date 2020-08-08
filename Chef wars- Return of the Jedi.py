for _ in range(int(input())):
    h,p=map(int,input().split())
    while p>0:
        h-=p 
        p/=2
        if h<=0:
            print("1")
            break
    else:
        print("0")
