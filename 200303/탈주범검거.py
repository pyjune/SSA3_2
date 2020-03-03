def f(N, M, R, C, L):
    q = [(R, C)]
    v = [[0]*M for _ in range(N)]
    v[R][C] = 1 # 시간
    pos = [0] *(L+1)  # 시간대별 가능 위치 수
    while q:
        i, j = q.pop(0)
        pos[v[i][j]] += 1 # 시간대에 도착하는 칸 번호
        if v[i][j] < L: # L초 미만에 도착한 칸이면
            for x in pipe[tunnel[i][j]]: # 파이프 모양에 따라 새롭게 진입할 칸 확인
                ni = i + di[x]
                nj = j + dj[x]
                if 0<=ni<N and 0<=nj<M and tunnel[ni][nj]!=0 and v[ni][nj]==0 and (x+2)%4 in pipe[tunnel[ni][nj]]:
                    v[ni][nj] = v[i][j] + 1 # 이동할 수 있는 칸에 시간
                    q.append((ni, nj))

    return sum(pos)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
pipe = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3],]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, R, C, L)
    print('#{} {}'.format(tc, r))
