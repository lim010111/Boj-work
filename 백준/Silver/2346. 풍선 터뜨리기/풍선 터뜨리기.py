from collections import deque


def solution(n, nums):
    result = []

    order = deque(range(1, n + 1))
    queue = deque(nums)
    while queue:
        selected = queue.popleft()
        order_selected = order.popleft()
        result.append(order_selected)

        if queue:
            if selected == 0:
                continue

            if selected > 0:
                while selected > 1:
                    queue.append(queue.popleft())
                    order.append(order.popleft())
                    selected -= 1

            if selected < 0:
                while selected:
                    queue.appendleft(queue.pop())
                    order.appendleft(order.pop())
                    selected += 1

    return result


n = int(input())
nums = list(map(int, input().split()))
answer = solution(n, nums)
print(*answer)