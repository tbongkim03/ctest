"""
예제 5-2
큐 연습

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
"""

# 기본 라이브러리 deque를 사용하는 이유?
# 리스트의 pop(0)은 시간복잡도가 O(n) 인데 반해, 데크의 popleft는 O(1) 이기 때문에 성능차이가 크다.
from collections import deque

# deque 객체 초기화
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # pop[0]
queue.append(1) 
queue.append(4)
queue.popleft() # pop[0]

# 먼저 들어온 순서대로 출력
print(list(queue))
queue.reverse()
# 나중에 들어온 순서부터 출력
print(list(queue))
