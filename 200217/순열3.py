def f(n, k):
    if n==k:
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            f(n+1, k)
            p[n], p[i] = p[i], p[n]

p = [1,2,3,4,5]
f(0, len(p))
