# 프로그래머스 체육복

def solution(n, lost, reserve):
    answer = 0
    cnt = [1 for _ in range(n)]  # 각자 학생들이 가진 체육복의 갯수
    for i in lost:  # 체육복 잃어버린 학생의 체육복 갯수 -1
        cnt[i - 1] -= 1
    for i in reserve:  # 체육복 여분 있는 학생의 체육복 갯수 +1
        cnt[i - 1] += 1

    for idx, (former, latter) in enumerate(zip(cnt, cnt[1:])): # 빌려줌
        if former == 2 and latter == 0:
            cnt[idx] -= 1
            cnt[idx + 1] += 1
        elif former == 0 and latter == 2:
            cnt[idx] += 1
            cnt[idx + 1] -= 1

    for i in cnt: # 수업 들을 수 있는 학생 수 카운트
        if i > 0:
            answer += 1

    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))