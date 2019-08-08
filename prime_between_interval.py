a,b=map(int,input().split())
if a<=100000 and b<=100000:
    for i in range(a+1,b):
        if i==1:
            print(1, end=" ")
        elif i==2:
            print(2, end=" ")
        elif i==3:
            print(3, end=" ")
        else:
            mid=i//2
            for j in range(2,mid+1):
                if (i%j) == 0:
                    break
            else:
                print(i,end=" ")
