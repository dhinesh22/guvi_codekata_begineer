a,b=map(int,input().split())
if a<=100000 and b<=100000:
    for i in range(a,b+1):
        if i%2==0:
            pass
        else:
            print(i,end=" ")
