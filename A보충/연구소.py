di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(lab, N, M):
    global maxV
    q = []
    visited = [[0]*M for _ in range(N)] # visited 생성
    for i in range(N): # 시작점 인큐 및 visited 표시
        for j in range(M):
            if lab[i][j]==2:
                q.append((i, j))
                visited[i][j] = 1
    while(len(q)!=0): # 큐가 비어있지 않으면 반복
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if lab[ni][nj]==0 and visited[ni][nj]==0: # 인접이면(빈공간이고 바이러스가 퍼지지 않았으면)
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    # 모든 칸에 대해 lab[i][j]와 visited[i][j]가 0인 칸 수를 maxV와 비교
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0 and visited[i][j]==0:
                cnt += 1
    if maxV<cnt:
        maxV = cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
pillar = []
for i in range(N):
    for j in range(M):
        if lab[i][j]==0: # 빈공간
            pillar.append((i, j)) # 기둥을 놓을 후보
for o in range(len(pillar)-2):
    for p in range(o+1, len(pillar)-1):
        for q in range(p+1, len(pillar)):
            lab[pillar[o][0]][pillar[o][1]] = 1
            lab[pillar[p][0]][pillar[p][1]] = 1
            lab[pillar[q][0]][pillar[q][1]] = 1
            bfs(lab, N, M)
            lab[pillar[o][0]][pillar[o][1]] = 0
            lab[pillar[p][0]][pillar[p][1]] = 0
            lab[pillar[q][0]][pillar[q][1]] = 0

# for i in range(N*M-2):
#     if lab[i//M][i%M]==0:
#         for j in range(i+1, N*M-1):
#             if lab[j // M][j % M] == 0:
#                 for k in range(j+1, N*M):
#                     if lab[k//M][k%M]==0:
#                         lab[i // M][i % M] = 1
#                         lab[j // M][j % M] = 1
#                         lab[k // M][k % M] = 1
#                         bfs(lab, N, M)
#                         lab[i // M][i % M] = 0
#                         lab[j // M][j % M] = 0
#                         lab[k // M][k % M] = 0
print(maxV)
