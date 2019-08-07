N=input()
l=len(N)
a = []
N=int(N)
temp=str(N)
new = ""
if l<=1000:
    while N!=0:
        lastdigit=N%10
        remdigit=N//10
        a.append(lastdigit)
        N=remdigit
    for i in a:
        i=str(i)
        new+=i
    if (new==temp):
        print('yes')
    else:
        print('no')
