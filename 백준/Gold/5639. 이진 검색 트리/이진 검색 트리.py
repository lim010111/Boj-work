import sys

sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data: int, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def make_tree():
    tree = {}
    root_node = int(input())
    tree[root_node] = Node(root_node)
    stack = [root_node]
    while True:
        try:
            input_node = input()
            input_node = int(input_node)
            tree[input_node] = Node(input_node)
            prev_node = None
            while True:
                if prev_node:
                    if not stack:
                        tree[prev_node].right = input_node
                        stack.append(input_node)
                        break
                    if input_node < stack[-1]:
                        tree[prev_node].right = input_node
                        stack.append(input_node)
                        break
                    else:
                        prev_node = stack.pop()
                else:
                    if input_node < stack[-1]:
                        tree[stack[-1]].left = input_node
                        stack.append(input_node)
                        break
                    else:
                        prev_node = stack.pop()

        except EOFError:
            break

    return tree, root_node


def post_order(node: Node) -> None:
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end="\n")


tree, root_node = make_tree()
post_order(tree[root_node])