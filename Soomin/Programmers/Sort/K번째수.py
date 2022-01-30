#20220130
#프로그래머스(정렬) : K번째수
#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(numbers):
    
    # *3
    nstr = list(map(lambda x: str(x) * 3, numbers))
    result = sorted(nstr, reverse=True)
    
    # *3한 부분 없애기
    result = list(map(lambda x: x[:len(x)//3], result))

    answer = str(int(''.join(result)))
    return answer