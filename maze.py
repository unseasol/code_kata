from collections import deque


def bfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # x축 델타, y축 델타
    # 델타 0,0왼쪽 1,1오른쪽, 2,2아래, 3,3위

    queue = deque()  # 큐생성
    queue.append((x, y))  # 큐에 탐색을 시작할 위치 넣어주고
    maze[x][y] = 1  # 시작 위치는 벽으로 막아버려 왜냐? 방문했다는 뜻
    while queue:  # 큐가 아직 있다면 while문은 멈추지 않는다.
        x, y = queue.popleft()
        if maze[x][y] == 3:
            return 1  # 만약 3(탈출구)면 끝냅시다.
        maze[x][y] = 1  # 방문한곳은 벽으로 막아버려
        for delta in range(4):  # 인접 4방향으로 델타기법
            visit_x, visit_y = x + dx[delta], y + dy[delta]
            if 0 <= visit_x < len(maze) and 0 <= visit_y < len(maze) and maze[visit_x][visit_y] != 1:
                queue.append((visit_x, visit_y))
    return 0


for _ in range(10):
    testcase = int(input())  # 몇 번째 testcase인지 입력 받고
    maze = [list(map(int, input())) for _ in range(100)]  # 미로 입력 받고
    x, y = 1, 1  # 시작점

    # 시작점이 1,1이 아니라면 시작점이 어디인지 찾아보자
    if maze[x][y] != 2:
        found = False
        for i in len(map):
            for j in len(map):
                if maze[i][j] == 2:
                    x, y = i, j
                    found = True
                    break
            if found == True:
                break  # 시작점 찾았으면 나오자

    print(f"#{testcase}", bfs(x, y))
