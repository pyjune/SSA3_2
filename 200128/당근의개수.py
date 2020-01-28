T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxIdx = 0 # 첫 번째를 가장 큰 자리로
    for i in range(1, N): # 나머지 자리와 비교
        if arr[maxIdx] < arr[i]: # arr[i]가 더 크면
            maxIdx = i
    print('#{} {} {}'.format(tc, maxIdx+1, arr[maxIdx]))
