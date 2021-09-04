```py

# 트리는 그래프와 결이 다름 - 생성법, 순회 방법 둘 다 다름
# 트리는 자식만 신경쓴다

1. 이진 트리 -> dfs 부분집합 트리와 같다.

1) 딕셔너리 이용 트리 만들기 -> 완전이진트리가 아닐 때
tree = defaultdict(list)
for _ in range(n):
    r, lt, rt = input().split()
    tree[r].append(lt)
    tree[r].append(rt)

-> 방향을 신경쓰지 않는다. 오로지 자식과의 관계만 생각함
{
  A : [B, C] // 자식은 B,C
  B : [D, .] // 자식은 D
  C : [E, F] ...
  D : [., .]
  E : [., .]
  F : [G, .]
  G : [., .]
}
      A
    /   \
   B     C
  /      /\
  D     E  F
            \
              G

1-1) 딕셔너리 트리 순회

-> 왼쪽 자식, 오른쪽 자식 각각 traverse 돌려주면 된다.

def preorder(v):
    print(v, end="")
    if tree[v][0] != ".":
        preorder(tree[v][0])
    if tree[v][1] != ".":
        preorder(tree[v][1])


2) 배열 이용 트리 만들기(완전 이진 트리만 가능)

tree = [1, 2, 3, 4, 5, 6, 7]

      1 (인덱스 : 0)
    /   \
   2     3
  /\      /\
4   5    6  7

2-1) 배열 이용 트리 순회
 def traverse(i, tree):
    if i < len(tree):
      print(tree[i])
      traverse(i * 2 + 1, tree)
      traverse(i * 2 + 2, tree)



3) 그래프 만드는 방법(인접리스트)으로 트리를 만들어야 할 경우도 있다.


4) 순회

전위 : 노드->왼트리->오트리
중위 : 왼트리->노드->오트리
후위 : 왼트리->오트리->노드


5) 순회결과 바탕으로 트리 생성

-> 중위 순회 결과 바탕으로 트리 생성 가능
-> 머지소트 하듯이 분할정복으로 mid 양옆으로 나눠주면 된다.

-> 이진탐색트리 전위 순회 바탕으로 트리 생성가능
-> 완전이진트리가 아니므로 i*2, i*2+1 이용 해야함


```
