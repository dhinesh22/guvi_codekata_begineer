a, b = map(int, input().split())
for j in range(a, b):
    temp = 0
    j = str(j)
    n = len(j)
    for i in j:
        i = int(i)
        temp += i**n
    temp = str(temp)
    if temp == j:
        print(j, end=" ")
