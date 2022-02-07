#20220207
#프로그래머스(2022 카카오 BLIND RECRUITMENT) : 양궁대회
#https://programmers.co.kr/learn/courses/30/lessons/92342
# 57.1점 #예시 테스트케이스는 통과

def kakao(a,n, info):
    result = [0,0,0,0,0,0,0,0,0,0,0]
    
    k = n
    
    for i in range(11):
        if info[i] == 0: #어피치 0일 때는 라이언이 1발 맞히는 것이 유리하다 판단
            result[i] = 1
            k -= 1
        else:
            if info[i] < a: #여기가 문제 #어피치가 특정값 이상으로 쏘면 그 점수는 공략 안하는 것이 유리?
                if k >= info[i] +1 :
                    result[i] = info[i] +1 #어피치보다 딱 1발 많이 쏘기
                    k -= result[i]
                                
        if k == 0:
            break
    
    # 화살을 다 쐈는지 확인
    zero = []
    nsum = n-sum(result)
    if sum(result) != n: #남은 화살이 있으면
        # 어피치가 화살을 쏜 점수의 인덱스
        for j in range(11):
            if info[j] != 0:
                zero.append(j)
        #만약 0점까지 쐈으면        
        if zero[-1] == 10:
            result[10] = n-sum(result) #라이언도 남은 화살 다 0에 쏨
        else:
            for i in range(n-sum(result)):
                if result[zero[-1]+i] == 10:
                    result[10] = nsum
                    break
                else:
                    result[zero[-1]+i] = 1 #어피치가 0발 쏜 곳에 1점씩
                    nsum -= 1
                    
                if nsum == 0:
                    break
    
    sum_apeach = 0
    sum_ryan = 0
    # 어피치 VS 라이언 점수 비교
    for i in range(11):
        if info[i] >= result[i]:
            if info[i] == 0 and result[i] == 0:
                continue
            else:
                sum_apeach += (10-i)
        else:
            sum_ryan += (10-i)
    # print(sum_apeach, sum_ryan)    
    if sum_apeach >= sum_ryan: #어피치가 이길 수밖에 없으면
        return [-1]
    else:
        return result

def solution(n, info):
    answer = []
    result2 = kakao(2, n, info)
    # print(result2)
    return result2
#     result3 = kakao(3, n, info)
    
#     if len(result2) == 1 and len(result3) == 1:
#         return result2
#     elif len(result2) == 11 and len(result3) == 1:
#         return result2
#     elif len(result2) == 1 and len(result3) == 11:
#         return result3
#     else:        
#         hap2 = 0
#         for i in range(11):
#             if info[i] < result2[i]:
#                 hap2 += (10-i)

#         hap3 = 0
#         for i in range(11):
#             if info[i] < result3[i]:
#                 hap3 += (10-i)
#         # print(hap2, hap3)
#         if hap2 >= hap3:
#             return result2
#         else:
#             return reulst3