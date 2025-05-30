"""
예제 5-8
dfs
"""

# 깊이 우선 탐색. 스택 자료구조에 기초함
# 재귀 함수를 이용했을 때 매우 간결하게 구현

# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    #해당 v 노드와 인접한 노드리스트에서 방문하지 않은 곳에서 재귀 호출
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def dfs_stack(graph, start, visited):
    # 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    stack = [start]
    while stack:
        # 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
        # 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
        v = stack.pop()
        # false 일 때
        if not visited[v]:
            print(v, end=' ')
            # 방문 처리를 하고
            visited[v] = True
            # 인접 노드를 스택에 넣기 // 중요한 점 : 스택은 나중에 들어온게 먼저 나가는 구조이기에 여러개 한번에 넣을때는 거꾸로 넣어줘야 원래 순서대로 나간다.
            stack.extend(reversed(graph[v]))
# graph의 노드는 1~8로, 0번은 빈 9개의 인덱스
graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

# 각 노드가 방문된 정보를 리스트 자료형으로 선언해놓기
visited = [False] * 9

# 호출
print("재귀를 이용한 dfs")
dfs(graph, 1, visited)

print("\n스택을 이용한 dfs")
visited = [False] * 9
dfs_stack(graph, 1, visited)

