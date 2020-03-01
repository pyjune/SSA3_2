
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    d = N//4
    num += num[:d]
    arr = []
    for i in range(d):
        for j in range(4):
            s = int(num[(i+j*d):(i+j*d)+d], 16)
            if s not in arr:
                arr.append(s)
    # arr.sort(reverse=True)
    # print('#{} {}'.format(tc, arr[K-1]))
    arr.sort()
    print('#{} {}'.format(tc, arr[len(arr)-K]))
