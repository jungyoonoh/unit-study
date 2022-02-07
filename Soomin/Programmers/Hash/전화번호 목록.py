#20220202
#프로그래머스(해시) : 전화번호 목록
#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):

    # sort 해주면 i와 i+1만 비교해도 됨
    phone_book.sort()
    # print(phone_book)
    # ['119', '1195524421', '97674223'] 이렇게 119 앞에 같은 것이 있다면 i+1에 올 수밖에 없다.
    for i in range(len(phone_book)-1):
        
        # 이중 for문 쓰면 효율성 떨어짐
        # for j in range(i+1,len(phone_book)):
        #     pb = phone_book[j]
        #     # print(phone_book[i],pb[:len(phone_book[i])])
        #     if phone_book[i] == pb[:len(phone_book[i])]:
        #         answer = False
        #         return answer
        #         exit(0)
        
        pb = phone_book[i+1]
        if phone_book[i] == pb[:len(phone_book[i])]:
            answer = False
            return answer
            exit(0)
            
    answer = True
    return answer