def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)



an = [1,2,3]
tr = [0]*2

comb(3, 2)

arr = [1,2,3,4,5]
c = [0]*3

def comb2(i, n, r):
    if i==r:
        print(c)
    else:
        for j in range(i, n-r+i+1):
            c[i] = arr[j]
            comb2(i+1, n, r)

comb2(0, 5, 3)
