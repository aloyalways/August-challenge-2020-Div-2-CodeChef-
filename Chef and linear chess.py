for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    step=float('inf')
    ans=-1
    for i in arr:
        if k>=i and k%i==0:
            if step>k//i:
                ans=i
                step=k//i
    print(ans)
