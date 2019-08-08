a,b=map(int,input().split())
if a<=100000 and b<=100000:
    for i in range(a+1,b):
        if i%2==0:
            print(i,end=" ")
        else:
            pass
            
