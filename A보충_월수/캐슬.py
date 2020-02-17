def shoot(s, tmp, N, M, D):
    minD = D+1 # 최소 거리값 초기화
    ti, tj = -1, -1 # 화살을 맞는 적의 좌표 후보
    for i in range(N):
        for j in range(M):
            if tmp[i][j]>0 and abs(i-N)+abs(j-s)<=D: # 사거리 이내의 적이 있으면
                if minD > abs(i-N)+abs(j-s):
                    ti, tj = i, j
                    minD = abs(i-N)+abs(j-s)
                elif minD == abs(i-N)+abs(j-s) and j<tj:
                    ti, tj = i, j
                    minD = abs(i - N) + abs(j - s)
    if ti>=0: # 화살을 맞는 적이 있으면
        tmp[ti][tj] += 1 # 화살을 맞은 표시를 남김
    # 화살에 맞은 적을 센 후 지우고,
    
    # 적을 성벽쪽으로 이동


def defence(s1, s2, s3, N, M, D):
    tmp = [[0]*M for _ in range(N)] # 게임판 선언
    for i in range(N):      # 초기 적의 배치를 복사해서 사용
        for j in range(M):
            tmp[i][j] = enemy[i][j]
    for _ in range(N): # 게임의 turn, 가장 윗줄의 적까지 공격
        shoot(s1, tmp, N, M, D) # tmp에서 화살을 맞은 적은 +1
        shoot(s2, tmp, N, M, D)
        shoot(s3, tmp, N, M, D)
        print()



N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]

# 궁수 배정
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            defence(i, j, k, N, M, D)
