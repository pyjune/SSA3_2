# 합이 10인 경우의 수...
def f(n, k, s): # 포함여부를 검토할 원소의 인덱스 n, 배열의 크기 k
                # n-1까지 고려한 부분집합의 합 s
    global cnt
    global ans
    cnt += 1
    if n==k: # 모든 원소가 고려되면
        if s==10:
            ans += 1
    elif s>10: # 이전에 고려한 원소의 합이 10보다 크면 중단
         return
    else:
        f(n+1, k, s) # n번 원소가 포함되지 않은 부분집합의 합
        f(n + 1, k, s + A[n])  # n번 원소가 포함된 부분집합의 합

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0
ans = 0
f(0, 10, 0)
print(ans, cnt)
