"""
예제 4-2
시각

정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.

00시 00분 03초
00시 13분 30초

반면에 다음은 3이 하나라도 포함되어 있지 않으므로 세면 안되는 시각이다.

00시 02분 55초
01시 27분 45초

첫째 줄에 정수 N이 입력된다 (0 <= N <= 23)
00시 00분 00초 부터 N시 59분 59초 까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

입력 예시
5

출력 예시
11475
"""

n = int(input())

cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
