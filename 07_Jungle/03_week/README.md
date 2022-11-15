# Jungle_03_week CheckPoint

### [1197 - MST](https://www.acmicpc.net/problem/1197)
- 크루스칼 알고리즘 : Kruskal's Algorithm
- 프림 알고리즘 : Prim's Algorithm
- **둘다 공부해야함**

### [1707 - 이분그래프](https://www.acmicpc.net/problem/1707)
- **이분 그래프** 학습!!!! ▶️ 문제만으로는 이해힘듬ㅠ
- 개같은 문제 이분그래프가 여러개인 경우도 만족함

### [21606 - 아침산책](https://www.acmicpc.net/problem/2606)
- **특별한 아이디어**
1. 인접한 실내 체크
2. 실외연결컴포넌트에 인접한 실내수 n
> n * (n - 1)

### [14888 - 연산자끼워넣기](https://www.acmicpc.net/problem/14888)
- `//` 나누기연산자
- 음수방향(좌측으로)
- ex)
1. 2018/5 = 403.6
2. 2018//5 = 403
3. -2018/5 = -403.6
4. -2018//5 = -404
5. int(-2018/5) = -403

### [2573 - 빙산](https://www.acmicpc.net/problem/2573)
- **기본로직1**
- while 문반복
    1. **Check compo** 
    - compo 개수 dfs으로 chk
    - compo 가 0인경우 **"0"출력 && Break**
    - compo 가 2이상인경우 **경과시간출력 && Break**
    2. **시간 + 1**
    3. **melting icebreg**
    - **오류** 녹아서 빙산이 0이되면 다음 재귀dfs에서 방문
    - 위의 경우를 방지하기위해서 녹아서 0이된 부분은 -1로 변환
    - '-1'이면 방문을 하지않음
    - **중요** 최종결과 table에서 -1인 부분을 0으로 다시 바꿈
- while문에서 출력 로직을 중간에 위치
    - 항상 마지막이나 처음에 위치시켰으나
    - 초기값에서 확인을 해주기위해서
    - while >>> [ 초기값 확인 > 출력 > 변환로직 ]
- **기본로직2**
    - 로직1은 Connected component의 갯수를 bfs/dfs 그리고 빙산지우기를 bfs/dfs 두번 돌렸었다.
    - 위로직을 빙산내부에서 돌리면서 component갯수와 빙산지우기 부분을 한번에 같이 체크해준다.

### [2617 - 구슬찾기](https://www.acmicpc.net/problem/2573)
- 그래프를 두가지 선언!!!
    - 무거운 방향 graph
    - 가벼운 방향 graph
- 모든 구슬에 대하여 heavy, light Graph를이용 하여 DFS or BFS 탐색
- 갯수가 (n - 1) // 2 보다 큰경우 불가능케이스

### [1916 - 최소비용 구하기](https://www.acmicpc.net/problem/1916)
- **다익스트라 Dijkstra**
- 1️⃣ : 그래프준비, dist리스트 INF로 초기화, 우선순위큐삽입
- 2️⃣ : 출발노드 설정, 출발노드 비용 0(dist[start] = 0)
- 3️⃣ : 힙큐에서 원소를 꺼내서 방문체크(+ 비용작은지 체크)
- 4️⃣ : 인접 노드의 비용이 이미 있는 작은지 체크
- 5️⃣ : 비용이 더 작은 경우 - 비용재할당, 큐에 삽입
- 6️⃣ : while 문으로 3, 4, 5 반복


 ### [2665 - 미로 만들기](https://www.acmicpc.net/problem/2665)
- **다익스트라 Dijkstra**
- 1️⃣ : board준비, visited 0으로 초기화, 우선순위큐삽입
    - (비용[벽부신수], ROW, COL)
- 2️⃣ : 4방향 ~ 범위체크, 방문체크
- 3️⃣ : 방문안했으면 체크하고 벽인지 아닌지 확인
- 4️⃣ : 벽인경우 (비용 + 1, nr, nc) 힙큐삽입
- 5️⃣ : 길인경우 (비용, nr, nc) 힙큐삽입
- 6️⃣ : while 문으로 2, 3, 4 반복
    - **BREAK POINT** : (N-1, N-1) 도달시 비용반환