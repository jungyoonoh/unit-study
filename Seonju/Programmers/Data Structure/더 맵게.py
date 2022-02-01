# 프로그래머스 더 맵게

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        cnt += 1

    if scoville[0] >= K:
        return cnt
    else:
        return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1, 1], 10))