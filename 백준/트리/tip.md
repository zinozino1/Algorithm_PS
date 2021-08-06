```py

# 트리는 그래프와 결이 다름 - 생성법, 순회 방법 둘 다 다름
# 트리는 자식만 신경쓴다

1. 이진 트리

1) 딕셔너리 이용 트리 만들기
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


2) 배열 이용 트리 만들기

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



```
