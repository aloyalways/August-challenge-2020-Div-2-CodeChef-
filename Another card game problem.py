for _ in range(int(input())):
    pc,pr=map(int,input().split())
    chef,rick=0,0
    left=pc%9
    if left>0:
        chef=1
        pc-=left
    chef+=pc//9
    left=pr%9
    if left>0:
        rick=1
        pr-=left
    rick+=pr//9
    if chef<rick:
        print("0 {}".format(chef))
    else:
        print("1 {}".format(rick))
