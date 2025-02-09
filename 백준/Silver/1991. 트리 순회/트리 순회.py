"""
Node class: Node 객체를 만드는 청사진이다.

Node 객체: 단일 노드의 자식 관계의 구조를 정의한다.

Node 객체를 담을 수 있는 공간, 트리
    - Key: 노드 값, Value: 노드 객체(노드 구조 설명)
"""

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def pre_order(node: Node) -> None:
    print(node.data, end="")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


def in_order(node: Node) -> None:
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end="")
    if node.right_node != None:
        in_order(tree[node.right_node])


def post_order(node: Node) -> None:
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end="")


n = int(input())
tree = {}

for _ in range(n):
    node, left_node, right_node = input().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    tree[node] = Node(node, left_node, right_node)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])