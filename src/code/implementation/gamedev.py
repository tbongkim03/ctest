"""
실전
게임 개발

캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로
이뤄진 N x M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A, B)로 나타낼 수 있고 A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼은 이러하다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터
차례대로 갈 곳을 정한다.

2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.

3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로
돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트 하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

입력 조건
첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
방향 d의 값으로는 다음과 같이 4가지가 존재한다.
- 0: 북쪽
- 1: 동쪽
- 2: 남쪽
- 3: 서쪽
셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터
남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어있다.
- 0: 육지
- 1: 바다
처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

입력 예시
4 4         # 4 x 4 맵 생성
1 1 0       # (1 , 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1     # 첫 줄은 모두 바다
1 0 0 1     # 둘째 줄은 바다 / 육지 / 육지 / 바다
1 1 0 1     # 셋째 줄은 바다 / 바다 / 육지 / 바다
1 1 1 1     # 넷째 줄은 모두 바다

출력 조건
첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
"""

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정하는 함수
def set_direction():
    global char_d, char_y, char_x
    global n, m
    # 맵의 외곽을 벗어나면 README.md 참조 // list out of range error
    yxW = [char_y, char_x-1] if 0 <= char_x-1 else [char_y, char_x]
    yxN = [char_y-1, char_x] if 0 <= char_y-1 else [char_y, char_x]
    yxE = [char_y, char_x+1] if char_x+1 <= m-1 else [char_y, char_x]
    yxS = [char_y+1, char_x] if char_y+1 <= n-1 else [char_y, char_x]
    # 0 : 3 > 2 > 1 > 0 서쪽부터
    if char_d == 0:
        directions = [3,2,1,0]
    # 1 : 0 > 3 > 2 > 1 북쪽부터
    elif char_d == 1:
        directions = [0,3,2,1] 
    # 2 : 1 > 0 > 3 > 2 동쪽부터
    elif char_d == 2:
        directions = [1,0,3,2]
    # 3 : 2 > 1 > 0 > 3 남쪽부터
    else:
        directions = [2,1,0,3]
    yx = [yxW, yxN, yxE, yxS]
    return directions, yx


# 2. 1번 함수에서 받은 방향순서대로 조회, 아직 가보지 않았다면, 회전, 전진
# 가본 칸이면, 회전만 수행, 1번을 다시 실행 == 다음 회전으로 하라는 말 [1,0,0,1] 이면 1에서 가본거니 0나올때 회전, 전진
def rotAndgo():
    global char_y, char_x, char_d, directions, yx, map_data
    global n, m
    # 회전 리스트순서대로 회전하면서 이동했을때 좌표 구해보기
    cnt = 0
    for d in directions:
        # W, N, E, S
        if d == 3:   # 서쪽부터
            ny, nx = yx[0][0], yx[0][1]    # 그 방향의 좌표값 [y, x]
        elif d == 0: # 북쪽부터
            ny, nx = yx[1][0], yx[1][1]
        elif d == 1: # 동쪽부터
            ny, nx = yx[2][0], yx[2][1]
        else:        # 남쪽부터
            ny, nx = yx[3][0], yx[3][1]
       
        # 맵의 외곽을 벗어나면 README.md 참조 // list out of range error
        if 0 <= ny <= n-1 and 0 <= nx <= m-1:
            # 바다이면, 가본칸이면
            if map_data[ny][nx] == 1 or map_data[ny][nx] == 2:
                cnt +=1
                continue
            else:
                # 가보지 않은 칸이면 이동 후 2로 바꾸기
                map_data[char_y][char_x] = 2
                char_y, char_x = ny, nx
                map_data[char_y][char_x] = 2
        else:
            cnt += 1
    # 모든 방향을 다 했는데 바다 or 가본칸
    if cnt == 4:
        backd = back()
        backy, backx = map(int, backd)
        # 뒤도 가본경우는 문제의 조건에 없지만,
        # 이것을 넣지 않으면 맵 외곽이 바다로 이루어 지지 않은 경우를
        # 해결할 수 없어서 넣었다.
        if map_data[backy][backx] == 1 or map_data[backy][backx] == 2:
            return 0
    return 1
# 3. 만약 모두 가본 칸이거나 바다로 되어 있는 칸 = 바라보는 방향은 유지, 뒤로 한칸 이동
# 뒤가 만약 바다면 가만히 있음
def back():
    global char_y, char_x, char_d
    # 캐릭터가 0일때, 1일때, 2일때, 3일떄 그 시계반대방향 이동 좌표
    # yx = [yxW서, yxN북, yxE동, yxS남]
    _, yx = set_direction()
    #print(char_d)
    if char_d == 0:
        backd = yx[3]
    elif char_d == 1:
        backd = yx[0]
    elif char_d == 2:
        backd = yx[1]
    else:
        backd = yx[2]
    return backd

n, m = map(int, input().split()) # 맵 크기 입력
char_y, char_x, char_d = map(int, input().split())
map_data = [0 for i in range(n)]
# n = 세로크기, m = 가로크기
# 세로로 몇줄 반복입력 받을까
for row in range(n):
    map_data[row] = list(map(int, input().split()))
while True:
    directions, yx = set_direction()
    rot = rotAndgo()
    result = 0
    for y in map_data:
        for x in y:
            if x == 2:
                result +=1
    if rot == 0:
        break
print(result)
for i in map_data:
    print(i)
