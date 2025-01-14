"""
예제 5-5
두 가지 방식으로 구현한 팩토리얼 예제

# 반복적으로 구현한 n!
# 재귀적으로 구현한 n!
"""

def factorial_using_for(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result
def factorial_using_recf(n):
    if n  <= 1:
        return 1 
    return n * factorial_using_recf(n - 1)

nFac = input("input n!(factorial) : ")
n = int(nFac[0])
result1 = factorial_using_for(n)
result2 = factorial_using_recf(n)
print("반복문을 사용해서 얻은 팩토리얼: ", result1)
print("재귀함수를 사용해서 얻은 팩토리얼: ", result2)
