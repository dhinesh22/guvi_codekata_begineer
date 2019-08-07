N=input()
l=len(N)
N=int(N)
if l<=1000:
    mid =N//2
    for i in range(1,mid+1):
        if N%i==0:
            print('yes')
        else:
            print('no')
