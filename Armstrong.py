a = input()
n = len(a)
temp = 0
if n <= 100000:
    for i in a:
        i = int(i)
        temp += i**n
    a = int(a)
    if temp == a:
        print('yes')
    else:
        print('no')
