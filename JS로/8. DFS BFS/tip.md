# DFS

## 중복순열

```js
function DFS(L, ans) {
    if (L == 3) {
        console.log(ans);
        return;
    } else {
        for (let i = 0; i <= arr.length - 1; i++) {
            ans.push(arr[i]);
            DFS(L + 1, ans);
            ans.pop();
        }
    }
}
```

## 순열

```js
let check = Array(arr.length).fill(0);

function DFS(L, ans) {
    // 3개 뽑는다
    if (L == 3) {
        // 전처리
        console.log(ans);
        return;
    } else {
        // arr.length 개 중에서
        for (let i = 0; i <= arr.length - 1; i++) {
            // 루프
            if (check[i] === 0) {
                check[i] = 1;
                ans.push(arr[i]);
                DFS(L + 1, ans);
                check[i] = 0;
                ans.pop();
            }
        }
    }
}
```

## 중복조합

### s, i 활용

```js
function DFS(L, s, ans) {
    if (L == 3) {
        console.log(ans);
        return;
    } else {
        for (let i = s; i <= arr.length - 1; i++) {
            ans.push(arr[i]);
            DFS(L + 1, i, ans);
            ans.pop();
        }
    }
}
```

## 조합

### s, i+1 활용

```js
function DFS(L, s, ans) {
    if (L == 3) {
        console.log(ans);
        return;
    } else {
        for (let i = s; i <= arr.length - 1; i++) {
            ans.push(arr[i]);
            DFS(L + 1, i + 1, ans);
            ans.pop();
        }
    }
}
```

## 격자탐색

```js
let arr = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
];

let check = Array(arr.length).fill(Array(arr.length).fill(0));

let dx = [0, 1, 0, -1];
let dy = [1, 0, -1, 0];
let cnt = 0;

function dfs(L, x, y) {
    if (x == arr.length - 1 && y == arr.length - 1) {
        cnt += 1;
    } else {
        for (let s = 0; s < 4; s++) {
            let ndx = x + dx[s];
            let ndy = y + dy[s];

            if (
                ndx <= arr.length - 1 &&
                ndx >= 0 &&
                ndy <= arr.length - 1 &&
                ndy >= 0 &&
                arr[ndx][ndy] === 0
            ) {
                arr[ndx][ndy] = 1;
                dfs(L + 1, ndx, ndy);
                arr[ndx][ndy] = 0;
            }
        }
    }
}
arr[0][0] = 1;
dfs(0, 0, 0);
```

# BFS

## 기본 BFS

```js
function bfs() {
    let q = [s];
    let visited = [s];
    let level = 1;

    while (q.length) {
        level++;
        for (let _ of q) {
            let curr = q.shift();
            if (curr === e) return level;

            for (let next of [curr - 1, curr + 1, curr + 5]) {
                if (visited.indexOf(next) === -1) {
                    visited.push(next);
                    q.push(next);
                }
            }
        }
    }
    return -1;
}
```

## 격자탐색

```js
function bfs(x, y) {
    let q = [];

    q.push([x, y]);
    check[x][y] = 1;

    while (q.length) {
        let [x, y] = q.shift();

        for (let s = 0; s < 4; s++) {
            nx = x + dx[s];
            ny = y + dy[s];

            if (nx < 0 || ny < 0 || nx >= arr.length || ny >= arr.length)
                continue;

            if (check[nx][ny] === 0 && arr[nx][ny] === 0) {
                check[nx][ny] = check[x][y] + 1;
                q.push([nx, ny]);
            }
        }
    }
}

bfs(0, 0);
```
