"""
예제 5-9
bfs
"""

# 너비 우선 탐색, 큐 자료구조에 기초함
# 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어 가까운 노드부터 탐색을 진행하게 된다.
# 선입 선출.

# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

from collections import deque

def bfs(graph, start, visited):
    # 시작 노드를 삽입한 큐 객체를 생성
    queue = deque([start])
    # 현재 노드를 방문처리를 한다.
    visited[start] = True

    # 큐에 값이 빌 때까지 반복
    while queue:
        # 선입 선출로 노드 추출
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드의 인접한 리스트에서 방문하지 않은 노드를 삽입하고 방문처리를 하기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
bfs(graph, 1, visited)
