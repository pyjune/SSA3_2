#5 6
#1 2 1 3 3 2 2 5 3 4 5 4

def dfs(n, V):
    visited[n] = 1 # n번 노드에 방문 표시
    print(n, end=' ') # n번 노드에서 할 일
    for i in range(1, V+1): # 모든노드 i에 대해
        if adj[n][i]==1 and visited[i]==0: # n에 인접하고, 방문하지 않았으면
            dfs(i, V) # i노드로 이동

#인접행렬 생성
V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
edge = list(map(int, input().split()))
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    #adj[n2][n1] = 1 # 방향성이 없으면
dfs(1, V)
