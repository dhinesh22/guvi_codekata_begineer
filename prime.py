N=input()
l=len(N)
N=int(N)
if l<=1000:
    mid =N//2
    for i in range(2,mid):
        if N%i==0:
            print('no')
            break
    else:
        print('yes')
        
