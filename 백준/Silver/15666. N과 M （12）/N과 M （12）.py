from typing import List


def findSequence(n: int, m: int, seq: List) -> None:
    if len(seq) == m:
        results.append(tuple(seq))
        return

    for num in nums:
        if seq and seq[-1] > num:
            continue

        seq.append(num)
        findSequence(n, m, seq)
        seq.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))

results = []
findSequence(n, m, [])
results = sorted(set(results))

for result in results:
    print(*result)