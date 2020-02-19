def dfs1(n, V, t):
    if n==t:  # 목적지에 방문한 경우
        return 1
    else:
        visited[n] = 1
        print(n, end = ' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: # 노드 i가 n에 인접이고 방문 전이면
                if dfs1(i, V, t) == 1: # i노드로 이동
                    return 1
        return 0 # dfs1이 1을 리턴한 적이 없으면(목적지를 방문하지 못하면)
    
def dfs2(n, V, t):
    s = []
    s.append(n) # 시작점 push()
    visited[n] = 1 # 스택에 저장됨
    while len(s)>0: # 스택에 방문할 노드(갈림길)가 남아있지 않으면
        n = s.pop()
        if n==t:
            return 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: # n번노드에서 갈수 있는 노드 i
                s.append(i)
                visited[i] = 1
    return 0

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
visited = [0]*(V+1)
for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향그래프

print(dfs1(1, V, 5))
print(dfs2(1, V, 5))
