"""
예제 5-4
재귀함수 종료 조건

100번 호출 후 종료하게 하는 재귀함수
"""

def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")
recursive_function(1)
