from sys import stdin
from collections import deque

input = stdin.readline


def solution(n, queue_or_stack, queuestack, m, elements):
    queue = deque(queuestack[index] for index, i in enumerate(queue_or_stack) if i == 0)
    returns = []
    for element in elements:
        queue.appendleft(element)
        returns.append(queue.pop())

    return returns




n = int(input())
queue_or_stack = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
m = int(input())
elements = list(map(int, input().split()))

print(*solution(n, queue_or_stack, queuestack, m, elements))