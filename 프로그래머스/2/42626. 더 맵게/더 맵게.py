import heapq

def solution(scoville, K):
    mix_count = 0
    scoville_heap = scoville[:]
    heapq.heapify(scoville_heap)

    while scoville_heap[0] < K:
        if len(scoville_heap) == 1:
            return -1
        first = heapq.heappop(scoville_heap)
        second = heapq.heappop(scoville_heap)
        mixed = first + second * 2
        heapq.heappush(scoville_heap, mixed)
        mix_count += 1

    return mix_count