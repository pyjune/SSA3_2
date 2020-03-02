di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rm = [list(map(int, input().split())) for i in range(N)]
    v = [0]*(N*N+1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N and rm[i][j]+1==rm[ni][nj]:
                    v[rm[i][j]] = 1
    cnt = 0
    maxV = 0
    st = 0
    for i in range(N*N, -1, -1): # v[1]이 가장 긴 구간의 시작인 경우 확인을 위해 v[0]까지 확인
        if v[i]==1:
            cnt += 1        # 연속한 1의 개수
        else:
            if maxV<=cnt:   # 길이가 같으면 왼쪽 구간 선택
                maxV = cnt  # 구간의 최대 길이
                st = i+1    # 가장 긴 구간의 시작 인덱스
            cnt = 0
    print('#{} {} {}'.format(tc, st, maxV+1))
