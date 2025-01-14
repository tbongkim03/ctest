"""
예제 5-1
스택 연습

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
"""

# 빈 리스트 초기화
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 정방향 리스트
print(stack)
# 역방향 리스트
print(stack[::-1])
